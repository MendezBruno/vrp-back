from typing import List
from pydantic import BaseModel, Field


class Leg(BaseModel):
    steps: List = Field(None, title='The distance traveled by this route leg, in float meters.')
    weight: float = Field(None, title='The calculated weight of the route leg.')
    distance: float = Field(None, title='The distance traveled by this route leg, in float meters.')
    summary: str = Field(None, title='Summary of the route taken as string. Depends on the summary parameter')
    duration: float = Field(None, title='The estimated travel time, in float number of seconds.')

    # def __init__(self, steps: List[Any], weight: float, distance: float, summary: str, duration: float,
    #              **data: Any) -> None:
    #     super().__init__(**data)
    #     self.steps = steps
    #     self.weight = weight
    #     self.distance = distance
    #     self.summary = summary
    #     self.duration = duration
    #
    # class Config:
    #     schema_extra = {
    #         "example": {
    #               "distance": 30.0,
    #               "duration": 100.0,
    #               "weight": 100.0,
    #               "steps": [],
    #               "summary": ""
    #         }
    #     }


class OrsmRoute(BaseModel):
    legs: List[Leg] = Field([], title='The whole geometry of the route value depending on overview parameter, '
                                        'format depending on the geometries parameter. See RouteStep\'s geometry '
                                        'property for a parameter documentation.')
    weight_name: str = Field(None, title='The name of the weight profile used during extraction phase.')
    weight: float = Field(None, title='The calculated weight of the route.')
    distance: float = Field(None, title='The distance traveled by the route, in float meters.')
    duration: float = Field(None, title='The estimated travel time, in float number of seconds.')
    geometry: dict = Field(None, title='The whole geometry of the route value depending on')

    # def __init__(self, legs: List[Leg], weight_name: str, weight: float, distance: float, duration: float,
    #              **data: Any) -> None:
    #     super().__init__(**data)
    #     self.legs = legs
    #     self.weight_name = weight_name
    #     self.weight = weight
    #     self.distance = distance
    #     self.duration = duration

    class Config:
        schema_extra = {
            "example": {
                "distance": 90.0,
                "duration": 300.0,
                "weight": 300.0,
                "weight_name": "duration",
                "geometry": {"type": "LineString",
                             "coordinates": [[120.0, 10.0], [120.1, 10.0], [120.2, 10.0], [120.3, 10.0]]},
                "legs": [
                    {
                        "distance": 30.0,
                        "duration": 100.0,
                        "steps": []
                    },
                    {
                        "distance": 60.0,
                        "duration": 200.0,
                        "steps": []
                    }
                ]
            }
        }


class Waypoint(BaseModel):
    hint: str
    waypoint_index: int = Field(0, description="Index of the point in the trip.")
    distance: float = Field(0, description="The distance, in metres, from the input coordinate to the snapped coordinate")
    location: List[float] = Field("", description="Float with la lat and lng")
    name: str = Field("", description="Name from street")


class OrsmRouteServiceResponseSchema(BaseModel):
    code: str = Field(None, title='if the request was successful Ok otherwise see the service dependent and general '
                                  'status codes.')
    waypoints: List[Waypoint] = Field(None, title=' Array of Waypoint objects representing all waypoints in order.')
    routes: List[OrsmRoute] = Field(None, title='An array of Route objects, ordered by descending recommendation rank.')

    # def __init__(self, code: str, waypoints: List[Waypoint], routes: List[OrsmRoute], **data: Any) -> None:
    #     super().__init__(**data)
    #     self.code = code
    #     self.waypoints = waypoints
    #     self.routes = routes
