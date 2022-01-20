from typing import List, Any


class Leg:
    steps: List[Any]
    weight: float
    distance: float
    summary: str
    duration: float

    def __init__(self, steps: List[Any], weight: float, distance: float, summary: str, duration: float) -> None:
        self.steps = steps
        self.weight = weight
        self.distance = distance
        self.summary = summary
        self.duration = duration


class Route:
    legs: List[Leg]
    weight_name: str
    weight: float
    distance: float
    duration: float

    def __init__(self, legs: List[Leg], weight_name: str, weight: float, distance: float, duration: float) -> None:
        self.legs = legs
        self.weight_name = weight_name
        self.weight = weight
        self.distance = distance
        self.duration = duration


class Waypoint:
    hint: str
    distance: float
    location: List[float]
    name: str

    def __init__(self, hint: str, distance: float, location: List[float], name: str) -> None:
        self.hint = hint
        self.distance = distance
        self.location = location
        self.name = name


class OrsmRouteServiceResponseSchema:
    code: str
    waypoints: List[Waypoint]
    routes: List[Route]

    def __init__(self, code: str, waypoints: List[Waypoint], routes: List[Route]) -> None:
        self.code = code
        self.waypoints = waypoints
        self.routes = routes
