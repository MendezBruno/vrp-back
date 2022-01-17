from fastapi.encoders import jsonable_encoder
from src.core.crud import jobs as cJobs
from src.core.schemas.Job import JobSchema, response_model, JobResponse, error_response_model
from fastapi import APIRouter, HTTPException, Path, FastAPI
from typing import List

router = APIRouter()


@router.post("/", response_model=JobResponse, status_code=201, response_description="Job data added into the database")
async def create_job(job: JobSchema):
    job = jsonable_encoder(job)
    new_job = await cJobs.add_job(job)
    return JobResponse(new_job, "create success")


@router.get("/", response_model=JobResponse, status_code=201, response_description="Jobs retrieved")
async def get_jobs():
    jobs = await cJobs.retrieve_jobs()
    if jobs:
        return JobResponse(jobs, "jobs data retrieved successfully")
    return JobResponse(jobs, "Empty list returned")


@router.get("/{id}", response_model=JobResponse, response_description="Job data retrieved")
async def get_student_data(id_job):
    student = await cJobs.retrieve_job(id_job)
    if student:
        return JobResponse(student, "Job data retrieved successfully")
    return error_response_model("An error occurred.", 404, "Job doesn't exist.")
