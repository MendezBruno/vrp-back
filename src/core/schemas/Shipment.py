from typing import List

from src.core.schemas.Shipment_step import Shipment_step


class Shipment:
    amount: List[int]
    skills: List[int]
    pickup: Shipment_step
    delivery: Shipment_step

    def __init__(self, amount: List[int], skills: List[int], pickup: Shipment_step, delivery: Shipment_step) -> None:
        self.amount = amount
        self.skills = skills
        self.pickup = pickup
        self.delivery = delivery