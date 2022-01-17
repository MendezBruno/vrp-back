from typing import List


class VehicleElement:
    id: int
    profile: str
    start: List[float]
    end: List[float]
    capacity: List[int]
    skills: List[int]
    time_window: List[int]

    def __init__(self, id: int, profile: str, start: List[float], end: List[float], capacity: List[int], skills: List[int], time_window: List[int]) -> None:
        self.id = id
        self.profile = profile
        self.start = start
        self.end = end
        self.capacity = capacity
        self.skills = skills
        self.time_window = time_window