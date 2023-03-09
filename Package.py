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
