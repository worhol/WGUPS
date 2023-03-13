from Truck import Truck
from LoadPackages import min_distance_from, distance_between
from datetime import datetime, timedelta
from LoadingData import load_package_data
from HashTable import HashTable


def truck_delivery(truck: Truck, packages_table: HashTable, start_time: datetime):
    load_package_data(packages_table)
    current_mileage = distance_between(truck.current_location, min_distance_from(truck))
    for n in range(len(truck.packages)):
        packages_table.lookup(truck.packages[n].id)[5] = "en route"
        packages_table.lookup(truck.packages[n].id)[6] = start_time.strftime("%I:%M:%S %p")

    delivered_packages=[]
    i=0
    while i < len(truck.packages):
        truck.packages[i].start_time=start_time.strftime("%I:%M:%S %p")
        packages_table.lookup(truck.packages[i].id)[8] = truck.packages[i].start_time
        time_hours = current_mileage / truck.speed  # hours
        time_minutes = int(time_hours * 60) % 60  # minutes
        time_seconds = int(time_hours * 3600) % 60  # seconds
        travel_time = timedelta(hours=time_hours, minutes=time_minutes, seconds=time_seconds)
        delivery_time = start_time + travel_time
        current_mileage += distance_between(truck.current_location, min_distance_from(truck))
        next_location = min_distance_from(truck)
        truck.current_location = next_location
        truck.packages[i].delivery_status = "delivered"
        truck.packages[i].delivered_at = delivery_time.strftime("%I:%M:%S %p")
        packages_table.lookup(truck.packages[i].id)[5] = truck.packages[i].delivery_status
        packages_table.lookup(truck.packages[i].id)[6] = truck.packages[i].delivered_at
        delivered_packages.append(truck.packages[i].id)
        truck.packages.pop(i)

    for n in delivered_packages:
        packages_table.lookup(n)[7] = current_mileage + distance_between(truck.current_location,
                                                                                                  '4001 South 700 East')