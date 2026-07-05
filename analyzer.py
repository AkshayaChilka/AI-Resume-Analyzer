import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "python", "sql", "fastapi", "flask", "django", "pandas",
    "numpy", "docker", "aws", "azure", "git", "nlp",
    "machine learning", "react", "javascript"
]

def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).lower().strip()

def extract_email(text: str):
    m = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return m.group(0) if m else None

def extract_phone(text: str):
    m = re.search(r"(\+?\d[\d\-\s()]{8,}\d)", text)
    return m.group(0) if m else None

def extract_name(text: str):
    doc = nlp(text[:1000])
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_skills(text: str):
    text_low = text.lower()
    return [skill for skill in SKILLS if skill in text_low]

def match_score(resume_text: str, job_text: str) -> float:
    vect = TfidfVectorizer(stop_words="english")
    tfidf = vect.fit_transform([resume_text, job_text])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(score * 100, 2)

def analyze_resume(resume_text: str, job_text: str):
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_text)

    resume_skills = extract_skills(resume_clean)
    job_skills = extract_skills(job_clean)

    missing_skills = list(set(job_skills) - set(resume_skills))

    return {
        "name": extract_name(resume_text),
        "email": extract_email(resume_text),
        "phone": extract_phone(resume_text),
        "skills": resume_skills,
        "missing_skills": missing_skills,
        "ats_score": match_score(resume_clean, job_clean)
    }