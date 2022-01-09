from typing import List, Optional


class Job:
    id: int
    service: int
    amount: List[int]
    location: List[float]
    skills: List[int]
    time_windows: Optional[List[List[int]]]

    def __init__(self, id: int, service: int, amount: List[int], location: List[float], skills: List[int], time_windows: Optional[List[List[int]]]) -> None:
        self.id = id
        self.service = service
        self.amount = amount
        self.location = location
        self.skills = skills
        self.time_windows = time_windows