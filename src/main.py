import uvicorn
from fastapi import FastAPI

from src.api.orsm.routes.router import orsm_router
from src.core.routes.router import jobs_router

app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

app.include_router(jobs_router, prefix="/jobs", tags=["jobs"])
app.include_router(orsm_router, prefix='/orsm', tags=["orsm"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
