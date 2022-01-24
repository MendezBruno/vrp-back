from typing import List, Any
from pydantic import BaseModel, Field


# profile = "driving"
# sanjuan = "-58.27611923217773,-34.7228847459182"
# federal = "-58.332080841064446,-34.75175051870402"
# roel = "-58.31324100494384,-34.78101155893815"
# myTuple = (sanjuan, federal, roel)
# # coordinates = "13.388860,52.517037;13.397634,52.529407;13.428555,52.523219"
# coordinates = ";".join(myTuple)
# alternative = "2"  # {true|false|number}
# step = "false"  # {true | false }
# geometry = "geojson"  # {polyline|polyline6|geojson}
# overview = "false"  # {full|simplified|false}
# annotation = "false"  # {true|false}


class OrsmRequest(BaseModel):
    profile: str = Field("driving", description='Route is transited by profile type')
    coordinates: List[Any] = Field(..., description='The coordinates calculate routes for.')
    alternatives: str = Field("false", description='Search for alternative routes. Passing a number alternatives=n searches for up to n alternative routes.')
    steps: str = Field("false", description='Returned route steps for each route leg')
    geometry: str = Field("geojson", description='Returned route geometry format (influences overview and per step)')
    overview: str = Field("simplified", description='Add overview geometry either full, simplified according to highest zoom level it could be display on, or not at all.')
    annotation: str = Field("false", description='Returns additional metadata for each coordinate along the route geometry.')

    def __init__(self, profile: str, coordinates: List[Any], alternatives: str, steps: str, geometry: str, overview: str, annotation: str, **data: Any) -> None:
        super().__init__(**data)
        self.profile = profile
        self.coordinates = coordinates
        self.alternatives = alternatives
        self.steps = steps
        self.geometry = geometry
        self.overview = overview
        self.annotation = annotation

    class Config:
        schema_extra = {
            "example": {
                "profile": "driving",
                "coordinates": "13.388860,52.517037;13.397634,52.529407;13.428555,52.523219",
                "alternatives": "false",
                "steps": "false",
                "geometry": "geojson",
                "overview": "false",
                "annotation": "false"
            }
        }
