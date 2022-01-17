from typing import List, Optional
from pydantic import BaseModel, Field


class JobSchema(BaseModel):
    id: int = Field(None, title='Id for job')
    service: int = Field(0, title='job service duration')
    amount: List[int] = Field([], title='an array of integers with level of package to deliver')
    location: List[float] = Field([], title='coordinates array')
    skills: List[int] = Field([], title='an array of integers defining mandatory skills')
    time_windows: Optional[List[List[int]]] = Field(None,
                                                    title='an array of time_window objects describing valid slots for '
                                                          'job service start')
    description: Optional[str] = Field([], title='a string describing this job')

    def __init__(self, id: int, service: int, amount: List[int], location: List[float], skills: List[int],
                 time_windows: Optional[List[List[int]]], description: Optional[str], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.id = id
        self.service = service
        self.amount = amount
        self.location = location
        self.skills = skills
        self.time_windows = time_windows
        self.description = description

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "service": 0,
                "amount": [1],
                "location": [34.0, 54.0],
                "skills": [1],
                "time_windows": [[300, 600]]
            }
        }


class UpdateJobSchema(BaseModel):
    pass


class JobResponse(BaseModel):
    job: dict
    code: int
    message: str

    def __init__(self, job: dict, code: int, message: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job: job
        self.code: code
        self.message: message



def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
