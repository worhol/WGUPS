# Samir Cokic
# Student ID: 010093856

from datetime import datetime

from Delivery import truck_delivery
from HashTable import HashTable
from Interface import menu, delivered_between
from LoadPackages import load_packages
from Truck import Truck

if __name__ == "__main__":
    # Creates object truck.
    truck1 = Truck()
    # Creates object truck.
    truck2 = Truck()
    # Creates object truck.
    truck3 = Truck()
    # Loads the packages onto each truck.
    load_packages(truck1, truck2, truck3)
    # Creates hash table object.
    packages_table = HashTable()
    # Sets the time when delivery starts
    start_time_1 = datetime(2023, 3, 10, 8, 0, 0)
    # Sets the time when delivery starts
    start_time_2 = datetime(2023, 3, 10, 9, 6, 0)
    # Sets the time when delivery starts
    start_time_3 = datetime(2023, 3, 10, 11, 0, 0)
    # First truck delivers the packages
    truck_delivery(truck1, packages_table, start_time_1)
    # Second truck delivers the packages
    truck_delivery(truck2, packages_table, start_time_2)
    # Third truck delivers the packages
    truck_delivery(truck3, packages_table, start_time_3)
    # Calls the user interface function
    menu(packages_table)
    # Checks for the statuses in timeframe
    # delivered_between("1203","1312",packages_table)