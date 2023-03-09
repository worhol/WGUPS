from Package import Package


class Truck:
    def __init__(self, current_location: str):
        self.current_location = current_location
        self.packages = []
        self.speed = 18

    def add_package(self, package: Package):
        self.packages.append(package)

    def __str__(self):
        package_info = "\n".join([str(package) for package in self.packages])
        return f" {package_info}"