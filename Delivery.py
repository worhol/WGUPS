from Truck import Truck
from LoadPackages import min_distance_from, distance_between
from datetime import datetime, timedelta
from LoadingData import load_package_data
from HashTable import HashTable


# The function truck_delivery takes three arguments: truck object, HashTable object and datetime
# and iterates through the content of truck, looking at the address of each package and decides
# which package will be delivered next based on the distance of the address on the package and current truck's address.
# Once the package is delivered it writes the delivery time to the HashTable.The function takes the argument
# start time of the delivery and writes it to the HashTable object. It also calculates the total mileage
# that truck traveled.
# Time complexity O(n^2). Space complexity O(n)
def truck_delivery(truck: Truck, packages_table: HashTable, start_time: datetime):
    # the function load package data loads the csv file into HashTable object that comes as the argument.
    load_package_data(packages_table)
    # variable current_mileage calls the function distance_between which takes the truck's current location as the
    # argument and then calls the min_distance_from function which returns the closest location of the undelivered
    # package that is on the truck. #distance_between then uses two arguments to calculate the traveled distance
    # between the truck's current location, which at the beginning is the hub and next location and assigns the result
    # as a current traveled mileage.
    current_mileage = distance_between(truck.current_location, min_distance_from(truck))

    # if the package with the id 9 is on the truck, it's wrong address gets corrected
    packages_table.lookup('9')[0] = "410 S State St"
    packages_table.lookup('9')[2] = 84111

    # all the packages that got loaded onto a truck have their current status "at the hub" the function enters the
    # loop that checks all the packages on the truck, and before they get delivered changes their status to "en route"
    # The packages also get their start time of the delivery recorded
    for n in range(len(truck.packages)):
        # The packages status gets recorded in the HashTable object
        packages_table.lookup(truck.packages[n].id)[5] = "en route"
        # The packages start time of the delivery gets recorded in the HashTable object
        packages_table.lookup(truck.packages[n].id)[6] = start_time.strftime("%I:%M:%S %p")

    # the list variable delivered_packages gets initiated. It will collect the information on total mileage that
    # the truck traveled
    delivered_packages = []

    # the function enters the while loop that goes through the packages on the truck and decides which package should
    # be delivered next, based on the minimum distance between the truck and the address of the package.
    i = 0
    while i < len(truck.packages):
        # Each package on the truck gets the start time of the delivery assigned as a string
        truck.packages[i].start_time = start_time.strftime("%I:%M:%S %p")
        # Start time gets recorded in the Hashtable object
        packages_table.lookup(truck.packages[i].id)[8] = truck.packages[i].start_time

        # Time spent on the delivery gets calculated based on the mileage that truck traveled,
        # and truck's speed which is 18 miles per hour
        time_hours = current_mileage / truck.speed  # hours
        time_minutes = int(time_hours * 60) % 60  # minutes
        time_seconds = int(time_hours * 3600) % 60  # seconds

        # travel_time variable gets assigned which uses timedelta function from python library to calculate the time
        # duration spent on the delivery between two locations
        travel_time = timedelta(hours=time_hours, minutes=time_minutes, seconds=time_seconds)

        # The delivery_time variable adds traveled time to start time to record the time of the delivery
        delivery_time = start_time + travel_time

        # The current_mileage gets updated with the addition of the distance that truck covered
        # between its current address and the delivery address
        current_mileage += distance_between(truck.current_location, min_distance_from(truck))

        # The next location that truck has to got to, gets assigned by calling the min_distance_from function,
        # that returns the next address closest to the truck
        next_location = min_distance_from(truck)

        # When truck delivers the package to the location, its current address becomes delivered package's address
        truck.current_location = next_location

        # Status of the delivered packages changes to "delivered"
        truck.packages[i].delivery_status = "delivered"

        # The time of the delivery for that package gets recorded
        truck.packages[i].delivered_at = delivery_time.strftime("%I:%M:%S %p")

        # The HashTable object gets updated with the new delivery status of the package as well as the time of the
        # delivery
        packages_table.lookup(truck.packages[i].id)[5] = truck.packages[i].delivery_status
        packages_table.lookup(truck.packages[i].id)[6] = truck.packages[i].delivered_at

        # delivered_packages list adds the delivered package id
        delivered_packages.append(truck.packages[i].id)

        # The delivered package gets removed from the truck's list of the packages that are on the truck
        truck.packages.pop(i)

    # Each package that was delivered gets the total mileage covered during the delivery of all the packages
    # assigned, and recorded in the HashTable object. Total mileage  during the delivery is calculated by adding to
    # the current_mileage the distance between the last address of the delivery and the address of the hub where
    # truck has to go after completion of the delivery.
    for n in delivered_packages:
        packages_table.lookup(n)[7] = current_mileage + distance_between(truck.current_location,
                                                                         '4001 South 700 East')
