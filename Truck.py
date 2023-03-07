from Package import Package


class Truck:
    def __init__(self, current_location: str, packages: Package):
        self.current_location = current_location
        self.packages = packages
