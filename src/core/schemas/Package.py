from pydantic import BaseModel, Field


class Package(BaseModel):
    id: int = Field(None, title='Id package')
    location: [] = Field([], title='lng and lat of deliver')
    address: str = Field("", title='address to deliver package')
    codePackage: int = Field(..., title='package array')

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "location": [34.0, 54.0],
                "address": "calle San juan 353, Quilmes",
                "packages": 12345
            }
        }


class PackageResponse(BaseModel):
    package: dict
    code: int
    message: str


def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
