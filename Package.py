import datetime


class Package:
    def __init__(self, id: int, address: str, city: str, state: str, zip: int, delivery_time: datetime,status: str, weight: int, instructions: str):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_time = delivery_time
        self.weight = weight
        self.status = status
        self.instructions = instructions

    def __str__(self):
        return f" {self.id} {self.address} {self.city} {self.state} {self.zip} {self.delivery_time} {self.weight} {self.status} {self.instructions}"
