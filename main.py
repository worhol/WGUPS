from HashTable import HashTable
from Package import Package
from LoadingData import load_package_data, load_distance_data, load_address_data
from LoadPackages import distance_between, min_distance_from, load_packages
from Truck import Truck

if __name__ == "__main__":
    truck1=Truck("410 S State St")
    truck2=Truck("410 S State St")
    truck3=Truck("410 S State St")
    load_packages(truck1,truck2,truck3)
    # print(distance_between("1330 2100 S", "2530 S 500 E"))
    # package = Package(5, "410 S State St", "Salt Lake City", "UT", 84111, "EOD", "5", "on truck")
    # truck = Truck("3595 Main St", package)
    # print(min_distance_from(truck))

    # distance_data = []
    # load_distance_data(distance_data)
    # for i in distance_data:
    #     print(i)
    # print(len(distance_data))
    # print(distance_data)

    # address_data = []
    # load_address_data(address_data)
    # for i in address_data:
    #     print(i)
    # my_table = HashTable()
    # load_package_data(my_table)
    # my_table.print_table()
    # print(my_table.lookup('2'))
    # print(my_table.lookup('2'))
    # my_table = HashTable()
    # my_table.insert("yes", 56)
    # my_table.print_table()
