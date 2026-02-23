from fastapi import FastAPI
from pydantic import BaseModel
from app.config import task_queue
from app.tasks import process_data

app = FastAPI()

class TaskRequest(BaseModel):
    value: int

@app.post("/submit")
def submit_task(request: TaskRequest):
    job = task_queue.enqueue(process_data, request.value)
    return {"job_id": job.id}

@app.get("/status/{job_id}")
def check_status(job_id: str):
    job = task_queue.fetch_job(job_id)
    if job:
        return {"status": job.get_status(), "result": job.result}
    return {"error": "Job not found"}
