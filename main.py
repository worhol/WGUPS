from HashTable import HashTable
from Package import Package
from LoadingData import load_package_data, load_distance_data, load_address_data
from LoadPackages import distance_between

if __name__ == "__main__":

    # print(distance_between("International Peace Gardens", "Salt Lake City Division of Health Services"))

    # distance_data = []
    # load_distance_data(distance_data)
    # for i in distance_data:
    #     print(i)
    # print(len(distance_data))
    # print(distance_data)

    address_data = []
    load_address_data(address_data)
    for i in address_data:
        print(i)
    # my_table = HashTable()
    # load_package_data(my_table)
    # my_table.print_table()

    # my_table = HashTable()
    # my_table.insert("yes", 56)
    # my_table.print_table()
