from fastapi.encoders import jsonable_encoder
from src.core.crud import jobs as c_jobs
from src.core.schemas.Job import JobSchema, JobResponse, error_response_model
from fastapi import APIRouter

jobs_router = APIRouter()


@jobs_router.post("/", response_model=JobResponse, status_code=201, response_description="Job data added into the database")
async def create_job(job: JobSchema):
    job = jsonable_encoder(job)
    new_job = await c_jobs.add_job(job)
    return JobResponse(new_job, 201, "create success")


@jobs_router.get("/", response_model=JobResponse, status_code=200, response_description="Jobs retrieved")
async def get_jobs():
    jobs = await c_jobs.retrieve_jobs()
    if jobs:
        return JobResponse(jobs, 200, "jobs data retrieved successfully")
    return JobResponse(jobs, 200, "Empty list returned")


@jobs_router.get("/{id_job}", response_model=JobResponse, response_description="Job data retrieved")
async def get_job_data(id_job):
    a_job = await c_jobs.retrieve_job(id_job)
    if a_job:
        return JobResponse(a_job, 200, "Job data retrieved successfully")
    return error_response_model("An error occurred.", 404, "Job doesn't exist.")
