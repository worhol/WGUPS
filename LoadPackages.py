import datetime

from LoadingData import load_address_data
from LoadingData import load_distance_data
from LoadingData import load_package_data
from Package import Package
from Truck import Truck
from HashTable import HashTable


def distance_between(address1: str, address2: str):
    address_list = []
    load_address_data(address_list)
    distance_list = []
    load_distance_data(distance_list)
    index1 = 0
    index2 = 0
    for address in address_list:
        if address1 == address[2]:
            index1 = int(address[0])
    for address in address_list:
        if address2 == address[2]:
            index2 = int(address[0])
    try:
        distance = distance_list[index2][index1]
    except IndexError:
        try:
            distance = distance_list[index1][index2]
        except IndexError:
            distance = -1
    return distance


#
# def min_distance_from(truck: Truck):
#     package_addresses = []
#
#     for package in truck.packages:
#         package_addresses.append(package.address)
#         # print(package.address)
#     addresses_distance = []
#     for address in package_addresses:
#         addresses_distance.append(distance_between(truck.current_location, address))
#     # print(addresses_distance)
#     # if min(addresses_distance)>0:
#     return package_addresses[addresses_distance.index(min(addresses_distance))]
def min_distance_from(truck: Truck):
    if not truck.packages:
        return None

    package_addresses = []
    for package in truck.packages:
        package_addresses.append(package.address)
    addresses_distance = []
    for address in package_addresses:
        addresses_distance.append(distance_between(truck.current_location, address))
    if min(addresses_distance)>0:
        return package_addresses[addresses_distance.index(min(addresses_distance))]


def load_packages(truck1: Truck, truck2: Truck, truck3: Truck):
    packages = []
    with open("packageCSV.csv", encoding='utf-8-sig') as file:
        for line in file:
            parts = line.strip().split(",")
            package = Package(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], "at the hub", parts[6],
                              parts[7],None)
            packages.append(package)

    for package in packages:
        if package.instructions.startswith("Delayed on flight") or package.instructions == "Wrong address listed":
            truck3.add_package(package)
        if package.instructions == "Can only be on truck 2":
            truck2.add_package(package)
        if package.delivery_time != "EOD" and package not in truck3.packages and package not in truck2.packages or package.id == '19':
            truck1.add_package(package)

    for package in packages:
        if len(truck2.packages) == 16:
            break
        if package not in truck1.packages and package not in truck3.packages and package not in truck2.packages:
            truck2.add_package(package)
    for package in packages:
        if len(truck3.packages) == 16:
            break
        if package not in truck1.packages and package not in truck3.packages and package not in truck2.packages:
            truck3.add_package(package)
