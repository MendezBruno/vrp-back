import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.jobs

jobs_collection = database.get_collection("jobs_collection")


# helpers


def job_helper(job) -> dict:
    return {
        "id": str(job["_id"]),
        "service": job["service"],
        "amount": job["amount"],
        "location": job["location"],
        "skills": job["skills"],
        "time_windows": job["time_windows"],
    }
