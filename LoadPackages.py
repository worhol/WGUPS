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
    recommended_address = address_list[index_distance][2]

    for row in enumerate(truck_load_table.data_map):
        if row[1] is not None:
            for k, v in row[1]:
                if v[0] == recommended_address:
                    return v[0]
