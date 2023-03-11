from Truck import Truck
from LoadPackages import min_distance_from, distance_between
from datetime import datetime, timedelta
from LoadingData import load_package_data
from HashTable import HashTable


def truck_delivery(truck: Truck, packages_table: HashTable, start_time: datetime):
    load_package_data(packages_table)
    i = 0
    current_mileage = distance_between(truck.current_location, min_distance_from(truck))
    while i < len(truck.packages):
        truck.packages[i].status = "en route"
        # print(truck.packages[i].status)
        # current_milage = distance_between(truck.current_location, min_distance_from(truck))
        time_hours = current_mileage / truck.speed  # hours
        time_minutes = int(time_hours * 60) % 60  # minutes
        time_seconds = int(time_hours * 3600) % 60  # seconds
        travel_time = timedelta(hours=time_hours, minutes=time_minutes, seconds=time_seconds)
        delivery_time = start_time + travel_time
        current_mileage += distance_between(truck.current_location, min_distance_from(truck))
        next_location = min_distance_from(truck)
        # print(truck.current_location+":"+next_location)
        # current_milage += distance_between(truck.current_location, next_location)
        # current_milage+=current_milage
        truck.current_location = next_location
        truck.packages[i].delivery_status = "delivered"
        truck.packages[i].delivered_at = delivery_time.strftime("%I:%M:%S %p")
        # truck.packages[i].delivery_status = "delivered at " + str(delivery_time.strftime("%I:%M:%S %p"))
        # print(truck.packages[i].delivery_status)
        # packages_table.data_map[truck.packages[i].id][5]=truck.packages[i].delivery_status
        packages_table.lookup(truck.packages[i].id)[5] = truck.packages[i].delivery_status
        packages_table.lookup(truck.packages[i].id)[6] = truck.packages[i].delivered_at
        # print("Package", truck.packages[i].id, truck.packages[i].delivery_status)
        truck.packages.pop(i)

    return current_mileage + distance_between(truck.current_location, '4001 South 700 East')
