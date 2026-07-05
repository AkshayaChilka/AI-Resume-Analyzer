# AI Resume Analyzer

An AI-powered resume analyzer that compares a resume with a job description and provides an ATS-style match score, missing skills, and improvement suggestions.

## Features
- Upload resume in PDF or DOCX format.
- Paste a job description for analysis.
- Extract name, email, phone, skills, and experience-related information.
- Calculate resume-job match score.
- Identify missing keywords and skills.
- Provide improvement suggestions.

## Tech Stack
- Python
- FastAPI
- PDF/DOCX parsing
- NLP
- SQL / SQLite
- HTML / CSS / JavaScript or Streamlit

## How It Works
1. User uploads a resume.
2. Resume text is extracted.
3. Job description is analyzed.
4. Skills and keywords are matched.
5. ATS-style score and feedback are generated.

## Project Structure
```text
resume_analyzer/
├── app/
├── uploads/
├── requirements.txt
└── README.md
```

## Installation
```bash
git clone https://github.com/yourusername/ai-resume-analyzer.git
cd ai-resume-analyzer
pip install -r requirements.txt
```

## Run the Project
```bash
uvicorn app.main:app --reload
```
## Live Demo
[Open the live app](http://127.0.0.1:8000/docs#/default/analyze_analyze_post)


## Example Output
- Resume Match Score: 72%
- Missing Skills: Docker, AWS, Tableau
- Suggestions: Add more project details and relevant keywords

## Future Improvements
- Add embeddings-based matching.
- Add downloadable PDF report.
- Add user login and analysis history.

## License
MIT
