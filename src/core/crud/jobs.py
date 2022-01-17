from bson.objectid import ObjectId

from src.core.crud.database import jobs_collection, job_helper


async def retrieve_jobs():
    jobs = []
    async for job in jobs_collection.find():
        jobs.append(job_helper(job))
    return jobs


# Add a new job into to the database
async def add_job(job_data: dict) -> dict:
    job = await jobs_collection.insert_one(job_data)
    new_job = await jobs_collection.find_one({"_id": job.inserted_id})
    return job_helper(new_job)


# Retrieve a job with a matching ID
async def retrieve_job(id_job: str) -> dict:
    job = await jobs_collection.find_one({"_id": ObjectId(id_job)})
    if job:
        return job_helper(job)


# Update a job with a matching ID
async def update_job(job_id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    job = await jobs_collection.find_one({"_id": ObjectId(job_id)})
    if job:
        updated_job = await jobs_collection.update_one(
            {"_id": ObjectId(job_id)}, {"$set": data}
        )
        if updated_job:
            return True
        return False


# Delete a job from the database
async def delete_job(job_id: str):
    job = await jobs_collection.find_one({"_id": ObjectId(job_id)})
    if job:
        await jobs_collection.delete_one({"_id": ObjectId(job_id)})
        return True
