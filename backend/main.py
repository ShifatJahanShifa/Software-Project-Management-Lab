from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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


@app.post("/generate", response_model=Response)
def generate(request: Request):
    response = generate_answer(request.question)
    return Response(answer=response)
