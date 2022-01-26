from typing import List, Any
from pydantic import BaseModel, Field

from src.core.schemas.Package import Package


class RouteRequest(BaseModel):
    paquerId: int = Field(..., title='Id for Paquer')
    packages: List[Package] = Field([], title='package array')

    class Config:
        schema_extra = {
            "example": {
                "paquerId": 12345,
                "packages": [{
                    "id": 1,
                    "location": [34.0, 54.0],
                    "address": "calle San juan 353, Quilmes",
                    "packages": 12345
                },
                    {
                        "id": 1,
                        "location": [34.0, 54.0],
                        "address": "calle San juan 353, Quilmes",
                        "packages": 12345
                    }]
            }
        }

class RouteSchema(BaseModel):
    id: int = Field(None, title='Id for Route')
    paquerId: int = Field(0, title='Id for Paquer')
    geojson: List[int] = Field([], title='geojson contains route package\'s')
    packages: List[Package] = Field([], title='package array')

    # def __init__(self, id: int, paquer_id: int, geojson: List[int], packages: List[Package], **data: Any) -> None:
    #     super().__init__(**data)
    #     self.id = id
    #     self.paquerId = paquer_id
    #     self.geojson = geojson
    #     self.packages = packages

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "paquerId": 12345,
                "geojson": [1],
                "packages": [{
                    "id": 1,
                    "location": [34.0, 54.0],
                    "address": "calle San juan 353, Quilmes",
                    "packages": 12345
                },
                    {
                        "id": 1,
                        "location": [34.0, 54.0],
                        "address": "calle San juan 353, Quilmes",
                        "packages": 12345
                    }]
            }
        }


class RouteResponse(BaseModel):
    route: dict = Field(..., title='the Route')
    code: int = Field(..., title='Response status code')
    message: str = Field(..., title='Message response')

    # def __init__(self, route: dict, code: int, message: str, **kwargs):
    #     super().__init__(**kwargs)
    #     self.route: route
    #     self.code: code
    #     self.message: message


def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
