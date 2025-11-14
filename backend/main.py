import os
import tempfile
import uuid

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from llm_service import generate_answer
from models import Request, Response

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Chatbot backend is running!"}


@app.post("/generate")
def generate(request: Request):
    code, extension = generate_answer(request.question)
    temp_dir = tempfile.gettempdir()
    file_id = str(uuid.uuid4())
    filename = f"{file_id}.{extension}"
    filepath = os.path.join(temp_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)

    return {
        "answer": code,
        "filename": filename,
        "extension": extension,
        "download_url": f"/download/{filename}",
    }


@app.get("/download/{filename}")
def download_file(filename: str):
    temp_dir = tempfile.gettempdir()
    filepath = os.path.join(temp_dir, filename)

    if not os.path.exists(filepath):
        return {"error": "File not found"}

    return FileResponse(
        path=filepath, media_type="application/octet-stream", filename=filename
    )
