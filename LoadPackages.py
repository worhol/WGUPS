from LoadingData import load_address_data
from LoadingData import load_distance_data


def distance_between(address1: str, address2: str):
    address_list = []
    load_address_data(address_list)
    distance_list = []
    load_distance_data(distance_list)
    index1 = 0
    index2 = 0
    for address in address_list:
        for i in address:
            if i==address1:
                index1 = int(address[0])
    for address in address_list:
        for i in address:
            if i == address2:
                index2 = int(address[0])
    distance = distance_list[index2][index1]
    return distance
