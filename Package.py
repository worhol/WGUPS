import datetime


class Package:
    def __init__(self, id: int, address: str, city: str, state: str, zip: int, delivery_time: str,status: str, weight: int, instructions: str, delivered_at: datetime, mileage: float, start_time:datetime):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_time = delivery_time
        self.weight = weight
        self.status = status
        self.instructions = instructions
        self.delivered_at = delivered_at
        self.mileage = mileage
        self.start_time = start_time

    def __str__(self):
        return f" {self.id} {self.address} {self.city} {self.state} {self.zip} {self.delivery_time} {self.weight} {self.status} {self.instructions} {self.delivered_at} {self.mileage} {self.start_time}"
