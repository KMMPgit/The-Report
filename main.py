from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fetcher import fetch_info
from summarizer import summarize
from generator import generate_documents
from emailer import send_email

app = FastAPI()

class ReportRequest(BaseModel):
    topic: str
    email: str | None = None

@app.post("/generate-report/")
def generate_report(request: ReportRequest):
    topic = request.topic
    try:
        raw_info = fetch_info(topic)
        summary = summarize(raw_info, topic)
        zip_path = generate_documents(topic, summary)
        if request.email:
            send_email(request.email, topic, zip_path)
        return {
            "message": "Report successfully generated",
            "summary": summary,
            "zip_file": zip_path
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
