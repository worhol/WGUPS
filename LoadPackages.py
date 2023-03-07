from LoadingData import load_address_data
from LoadingData import load_distance_data
from LoadingData import load_package_data
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


def min_distance_from(truck: Truck):
    address_list = []
    load_address_data(address_list)
    distance_list = []
    load_distance_data(distance_list)
    truck_index = 0
    truck_load_table = HashTable()
    load_package_data(truck_load_table)
    # min_distance = 0
    for address in address_list:
        if truck.current_location in address:
            truck_index = int(address[0])
    min_distance = min(d for d in distance_list[truck_index] if d > 0)

    index_distance = 0
    for i in range(len(distance_list[truck_index])):
        if distance_list[truck_index][i] == min_distance:
            index_distance = i
    recommended_address = address_list[index_distance][1]

    # for packages in truck_load_table:
    #     for package in packages:
    #         if package.address == recommended_address:
    #             return package.address
    # return truck_load_table.lookup('2')
    package_ids = []
    for i in range(len(truck_load_table.data_map)):
        if truck_load_table.data_map[i] is not None:
            for j in range(len(truck_load_table.data_map[i])):
                package_id = truck_load_table.lookup(truck_load_table.data_map[i][j][0])
                package_ids.append(package_id)
            return package_id[0]
    # matching_packages = []
    # for package_id in package_ids:
    #     package = truck_load_table.lookup(package_id)
    #     if package.address == recommended_address:
    #         matching_packages.append(package)
    # return [package.address for package in matching_packages]
