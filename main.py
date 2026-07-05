import os
import shutil
from fastapi import FastAPI, UploadFile, File, Form
from app.parser import extract_text
from app.analyzer import analyze_resume

app = FastAPI(title="AI Resume Analyzer")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...), job_description: str = Form(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text(file_path)
    result = analyze_resume(resume_text, job_description)

    return result