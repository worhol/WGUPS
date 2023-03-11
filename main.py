import Delivery as Delivery

from HashTable import HashTable
from Package import Package
from LoadingData import load_package_data, load_distance_data, load_address_data
from LoadPackages import distance_between, min_distance_from, load_packages
from Truck import Truck
from Delivery import truck_delivery
from datetime import datetime
from Interface import menu

if __name__ == "__main__":
    truck1 = Truck()
    truck2 = Truck()
    truck3 = Truck()
    load_packages(truck1, truck2, truck3)
    packages_table = HashTable()
    start_time = datetime(2023, 3, 10, 8, 0, 0)
    start_time3 = datetime(2023, 3, 10, 9, 6, 0)
    truck_delivery(truck1, packages_table,start_time)
    # print(min_distance_from(truck1))
    truck_delivery(truck2, packages_table, start_time)
    truck_delivery(truck3, packages_table,start_time3)
    packages_table.print_table()
    # print(truck_delivery(truck1, packages_table,start_time)+truck_delivery(truck2, packages_table, start_time)+truck_delivery(truck3, packages_table, start_time3))
    # menu(start_time,packages_table)
    # truck4 = Truck()
    # start_time4=datetime(2023, 3, 12, 9, 0, 0)
    # truck_delivery(truck4, packages_table, start_time4)
    # print(packages_table.lookup('1'))
    # print(packages_table.lookup('6'))
    # print(packages_table.lookup('13'))
    # print(packages_table.lookup('14'))
    # print(packages_table.lookup('16'))
    # print(packages_table.lookup('20'))
    # print(packages_table.lookup('25'))
    # print(packages_table.lookup('29'))
    # print(packages_table.lookup('30'))
    # print(packages_table.lookup('31'))
    # print(packages_table.lookup('34'))
    # print(packages_table.lookup('37'))
    # print(packages_table.lookup('40'))
    # print(packages_table.lookup('19'))














    # print(len(truck1.packages)+len(truck2.packages)+len(truck3.packages))

    # print(distance_between("4001 South 700 East", truck1.packages[12].address))
    # print(truck1.packages[12].address)
    # print(min_distance_from(truck3))
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
