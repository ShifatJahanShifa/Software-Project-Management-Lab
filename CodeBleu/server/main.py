import os
import tempfile

from comment_cleaner import remove_comments
from constants import SUPPORTED_CODE_FILES
from extension_extractor import get_language_from_extension
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from tokenizer import custom_tokenizer

from codebleu import calc_codebleu

app = FastAPI(title="CodeBLEU Scorer Backend")

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/codebleu-score")
async def score(
    candidate_file: UploadFile = File(...), reference_file: UploadFile = File(...)
):
    try:
        candidate_extension = os.path.splitext(candidate_file.filename)[1].lower()
        reference_extension = os.path.splitext(reference_file.filename)[1].lower()

        if candidate_extension not in SUPPORTED_CODE_FILES:
            raise HTTPException(
                status_code=400,
                detail=f"Candidate file extension '{candidate_extension}' is not supported.",
            )
        if reference_extension not in SUPPORTED_CODE_FILES:
            raise HTTPException(
                status_code=400,
                detail=f"Reference file extension '{reference_extension}' is not supported.",
            )
        if candidate_extension != reference_extension:
            raise HTTPException(
                status_code=400,
                detail=f"Candidate language '{candidate_extension}' does not match reference language '{reference_extension}'.",
            )

        with tempfile.NamedTemporaryFile(
            delete=False, suffix=os.path.splitext(candidate_file.filename)[1]
        ) as tmp_candidate:
            candidate_path = tmp_candidate.name
            tmp_candidate.write(await candidate_file.read())

        with tempfile.NamedTemporaryFile(
            delete=False, suffix=os.path.splitext(reference_file.filename)[1]
        ) as tmp_reference:
            reference_path = tmp_reference.name
            tmp_reference.write(await reference_file.read())

        with open(candidate_path, "r", encoding="utf-8") as f:
            candidate_code = f.read()

        with open(reference_path, "r", encoding="utf-8") as f:
            reference_code = f.read()

        language = get_language_from_extension(candidate_file.filename)
        candidate_code_clean = remove_comments(candidate_code, language)
        reference_code_clean = remove_comments(reference_code, language)

        candidate_code_clean = custom_tokenizer(candidate_code_clean)
        reference_code_clean = custom_tokenizer(reference_code_clean)

        candidate_code_clean = " ".join(candidate_code_clean)
        reference_code_clean = " ".join(reference_code_clean)

        candidate_list = [candidate_code_clean]
        reference_list = [[reference_code_clean]]

        weights = (0.25, 0.25, 0.25, 0.25)
        result = calc_codebleu(
            reference_list, candidate_list, lang=f"{language.strip()}", weights=weights
        )
    
        print(result)
        return JSONResponse(content=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if os.path.exists(candidate_path):
            os.remove(candidate_path)
        if os.path.exists(reference_path):
            os.remove(reference_path)
