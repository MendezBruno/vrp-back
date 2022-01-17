from typing import List


class Shipment_step:
    id: int
    service: int
    location: List[float]

    def __init__(self, id: int, service: int, location: List[float]) -> None:
        self.id = id
        self.service = service
        self.location = location
