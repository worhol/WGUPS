from Package import Package


# This class is a blueprint for the Truck object
class Truck:
    def __init__(self):
        # Starting location of the truck is at the hub
        self.current_location = "4001 South 700 East"
        # This list is used to add packages to it
        self.packages = []
        # Speed of the truck
        self.speed = 18

    # This method takes Package object as an argument and adds it to the truck
    def add_package(self, package: Package):
        self.packages.append(package)

    # This is the string method for Truck class
    def __str__(self):
        package_info = "\n".join([str(package) for package in self.packages])
        return f" {package_info}"
