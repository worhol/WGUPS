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
        for i in address:
            if i == address1:
                index1 = int(address[0])
    for address in address_list:
        for i in address:
            if i == address2:
                index2 = int(address[0])
    distance = distance_list[index2][index1]
    return distance


# def min_distance_from(truck: Truck):
#     address_list = []
#     load_address_data(address_list)
#     distance_list = []
#     load_distance_data(distance_list)
#     truck_index = 0
#     truck_load_table = HashTable()
#     load_package_data(truck_load_table)
#     for address in address_list:
#         if truck.current_location in address:
#             truck_index = int(address[0])
#     min_distance = min(d for d in distance_list[truck_index] if d > 0)
#
#     index_distance = 0
#     for i in range(len(distance_list[truck_index])):
#         if distance_list[truck_index][i] == min_distance:
#             index_distance = i
#     recommended_address = address_list[index_distance][2]
#
#     for row in enumerate(truck_load_table.data_map):
#         if row[1] is not None:
#             for k, v in row[1]:
#                 if v[0] == recommended_address:
#                     return v[0]
#
def min_distance_from(truck: Truck):
    address1 = truck.current_location


def load_packages(truck1: Truck, truck2: Truck, truck3: Truck):
    packages = HashTable()
    info = []
    load_package_data(packages)
    for i in range(len(packages.data_map)):
        if packages.data_map[i] is not None:
            for package in packages.data_map[i]:
                if 'Can only be on truck 2' in package[1]:
                    truck2.add_package(package)
                if 'Delayed on flight---will not arrive to depot until 9:05 am' in package[1]:
                    truck3.add_package(package)
                if package[1][6].startswith('"Must be delivered'):
                    truck1.add_package(package)
    print(len(truck2.packages))
    print(len(truck3.packages))
    print(len(truck1.packages))

    # truck1 = []
    # truck2 = []
    # truck3 = []
    # temp = []
    # for package in packages:
    #     for i in package:
    #         if i.startswith('"Must be delivered'):
    #             truck1.append(package)
    # for package in packages:
    #     if "EOD" in package and package not in truck1:
    #         if package[0] == '19':
    #             continue
    #         temp.append(package)
    # for package in packages:
    #     if package not in temp and package not in truck1 and 'Delayed on flight---will not arrive to depot until 9:05 am' not in package:
    #         truck1.append(package)
    #
    # for package in packages:
    #     if 'Delayed on flight---will not arrive to depot until 9:05 am' in package or 'Wrong address listed' in package:
    #         truck3.append(package)
    # truck = Truck("410 S State St", temp)
    # for package in truck.packages:
    #     print(package)
    # print(distance_between('2835 Main St', temp[1][1]))
    # for i in range(len(temp)):
    # package = Package(5, "410 S State St", "Salt Lake City", "UT", 84111, "EOD", "5", "on truck")
    # truck_to_go=Truck("3148 S 1100 W", package)
    # print(min_distance_from(truck_to_go))

    # print(len(temp))
    # for package in truck1:
    #     print(package)
    # print(len(truck1))
    # for package in morning:
    #     print(package)
    # print()
    # for package in truck2:
    #     print(package)
    # print(len(truck2))
    # print(len(eod))
    # print(len(morning))
    # for package in temp:
    #     print(package)
    # print(len(temp))
