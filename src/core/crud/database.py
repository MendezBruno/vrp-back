import motor.motor_asyncio

from src.core.env import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.db_url)

database = client.jobs

jobs_collection = database.get_collection("jobs_collection")
routes_collection = database.get_collection("routes_collection")


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


def route_helper(route) -> dict:
    return {
        "id": str(route["_id"]),
        "paquerId": route["paquerId"],
        "geojson": route["geojson"],
        "packages": route["packages"]
    }
