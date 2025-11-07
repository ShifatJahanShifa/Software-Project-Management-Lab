from fastapi import FastAPI
from llm_service import generate_answer
from models import Request, Response

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Chatbot backend is running!"}


@app.post("/generate", response_model=Response)
def generate(request: Request):
    response = generate_answer(request.question)
    return Response(answer=response)
