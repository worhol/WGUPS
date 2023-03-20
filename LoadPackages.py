import datetime

from LoadingData import load_address_data
from LoadingData import load_distance_data
from LoadingData import load_package_data
from Package import Package
from Truck import Truck
from HashTable import HashTable


# This function takes two addresses as the arguments and returns the distance between them.
# Time complexity O(n). Space complexity O(n^2)
def distance_between(address1: str, address2: str):
    # Creates empty list for addresses
    address_list = []
    # Calls the load_address_data function that populates the address_list from the csv
    load_address_data(address_list)
    # Creates empty list for distances
    distance_list = []
    # Calls the load_distance_data function that populates the distance_list from the csv
    load_distance_data(distance_list)
    # Two variables index1 and index2 that will track the indexes of the distances are initialized and set to 0
    index1 = 0
    index2 = 0
    # The function enters the loop through the addresses list and looks for the index of the first address
    for address in address_list:
        if address1 == address[2]:
            index1 = int(address[0])
    # The function enters the loop through the addresses list and looks for the index of the second address
    for address in address_list:
        if address2 == address[2]:
            index2 = int(address[0])

    # The function tries to get the distance from the distance_list which is a distance matrix,
    # by accessing the list using the index1 and index2. If that raise the IndexError, indexes are flipped.
    # if the addresses are not in the address list and their index is not valid, the function returns -1
    try:
        distance = distance_list[index2][index1]
    except IndexError:
        try:
            distance = distance_list[index1][index2]
        except IndexError:
            distance = -1
    return distance


# This function takes the Truck object as the argument then returns the nearest address
# for the delivery based on the addresses of packages loaded on the truck.
# Time complexity O(n). Space complexity O(n)
def min_distance_from(truck: Truck):
    # The function first checks if there are packages on the truck. If the truck is empty it returns None
    if not truck.packages:
        return None

    # Creates empty list for storing the addresses of the packages
    package_addresses = []

    # The function loops through the packages loaded on the truck and adds each package address to the
    # package_address list
    for package in truck.packages:
        package_addresses.append(package.address)

    # Creates the empty list for storing the distances
    addresses_distance = []

    # The function loops through package_address list, calls the distance_between function and takes truck's current
    # address and each address in the list as the arguments and adds the distance to the address distance list
    for address in package_addresses:
        addresses_distance.append(distance_between(truck.current_location, address))
    # The function checks if the distance is greater than zero, and looks for the minimum distance in the address
    # distance list. It takes the index of the distance from the  address_distance list and return the address
    # associated with that index in the package_address list
    if min(addresses_distance) > 0:
        return package_addresses[addresses_distance.index(min(addresses_distance))]


# This function takes the three Truck objects as the arguments,
# then assigns the packages to each one based on the specific instructions.
# Time complexity O(n^2). Space complexity O(n)
def load_packages(truck1: Truck, truck2: Truck, truck3: Truck):
    # Creates empty list packages
    packages = []
    # Opens the csv file and loops through each line, then splits the line by commas, then creates new Package object
    # and adds parts to the Package object. Package object gets added to the packages list
    with open("packageCSV.csv", encoding='utf-8-sig') as file:
        for line in file:
            parts = line.strip().split(",")
            package = Package(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], "at the hub", parts[6],
                              parts[7], None, 0.0, None)
            packages.append(package)
    # Creates the empty list packages_to_remove_1 that will contain packages that can be removed from the packages list
    packages_to_remove_1 = []
    # Loops through the packages list and checks for the instructions. Those that match gets added to the truck3 and
    # to the packages_to_remove_1
    for package in packages:
        if (package.instructions.startswith(
                "Delayed on flight") and package.delivery_time == "EOD") or package.instructions == "Wrong address listed":
            truck3.add_package(package)
            packages_to_remove_1.append(package)
    # Loops through the packages_to_remove_1 and removes the package from packages list
    for package in packages_to_remove_1:
        packages.remove(package)

    # Creates the empty list packages_to_remove_2 that will contain packages that can be removed from the packages list
    packages_to_remove_2 = []

    # Loops through the packages list and checks for the instructions. Those that match gets added to the truck2 and
    # to the packages_to_remove_2
    for package in packages:
        if package.instructions == "Can only be on truck 2" or package.instructions.startswith("Delayed on flight"):
            truck2.add_package(package)
            packages_to_remove_2.append(package)

    # Loops through the packages_to_remove_2 and removes the package from packages list
    for package in packages_to_remove_2:
        packages.remove(package)

    # Creates the empty list packages_to_remove_3 that will contain packages that can be removed from the packages list
    packages_to_remove_3 = []

    # Loops through the packages list and checks for the instructions. Those that match gets added to the truck1 and
    # to the packages_to_remove_3
    for package in packages:
        if package.delivery_time != "EOD" or package.id == '19':
            truck1.add_package(package)
            packages_to_remove_3.append(package)

    # Loops through the packages_to_remove_3 and removes the package from packages list
    for package in packages_to_remove_3:
        packages.remove(package)

    # Loops through the truck1 packages and if the same address was found in the packages, that package gets loaded
    # to the truck while the truck is not full. Package gets removed from the package list.
    for pack in truck1.packages:
        # Truck is full when it contains 16 packages. The loop breaks at that moment.
        if len(truck1.packages) == 16:
            break
        for package in packages:
            if pack.address == package.address:
                truck1.add_package(package)
                packages.remove(package)
    # Loops through the truck2 packages and if the same address was found in the packages, that package gets loaded
    # to the truck while the truck is not full. Package gets removed from the package list.
    for pack in truck2.packages:
        # Truck is full when it contains 16 packages. The loop breaks at that moment.
        if len(truck2.packages) == 16:
            break
        for package in packages:
            if pack.address == package.address:
                truck2.add_package(package)
                packages.remove(package)

    # Loops through the truck3 packages and if the same address was found in the packages, that package gets loaded
    # to the truck while the truck is not full. Package gets removed from the package list.
    for pack in truck3.packages:
        # Truck is full when it contains 16 packages. The loop breaks at that moment.
        if len(truck3.packages) == 16:
            break
        for package in packages:
            if pack.address == package.address:
                truck3.add_package(package)
                packages.remove(package)

    # Creates the empty list packages_to_remove_4 that will contain packages that can be removed from the packages list
    packages_to_remove_4 = []

    # Loops through the leftover packages and fills up the truck until the truck is full.
    for package in packages:
        # Truck is full when it contains 16 packages. The loop breaks at that moment.
        if len(truck2.packages) == 16:
            break
        truck2.add_package(package)
        packages_to_remove_4.append(package)

    # Loops through the packages_to_remove_4 and removes the package from packages list
    for package in packages_to_remove_4:
        packages.remove(package)

    # Creates the empty list packages_to_remove_5 that will contain packages that can be removed from the packages list
    packages_to_remove_5 = []

    # Loops through the leftover packages and fills up the truck.
    for package in packages:
        truck3.add_package(package)
        packages_to_remove_5.append(package)

    # Loops through the packages_to_remove_5 and removes the package from packages list
    for package in packages_to_remove_5:
        packages.remove(package)
