from datetime import datetime
from HashTable import HashTable


def menu(table: HashTable):
    print("1. Print All Package Status and Total Mileage\n2. Get a Single Package Status with a "
          "Time\n3."
          "Get All Package Status with a Time\n4. Exit the Program")
    user_input = int(input("Enter your choice:"))
    if user_input == 1:
        mileage = []
        for i in range(1, len(table.data_map)):
            mileage.append(table.lookup(str(i))[7])
            print(
                f"Package ID: {str(i)}, Address: {table.lookup(str(i))[0]}, {table.lookup(str(i))[1]}, {table.lookup(str(i))[2]}, weight: {table.lookup(str(i))[4]}, delivery deadline: {table.lookup(str(i))[3]} was {table.lookup(str(i))[5]} at {table.lookup(str(i))[6]}.")
        print()
        print(f"TOTAL MILEAGE IS: {sum(set(mileage))}")
    if user_input == 2:
        package_id = str(input("Please enter the package ID: "))
        time_of_inquiry = input("Enter the time in military time, i.e., 0900: ")
        time_of_inquiry_obj = datetime.strptime(time_of_inquiry, '%H%M')
        if table.lookup(package_id) is not None:
            delivery_start = datetime.strptime(table.lookup(package_id)[8], "%I:%M:%S %p")
            delivery_end = datetime.strptime(table.lookup(package_id)[6], "%I:%M:%S %p")
            if delivery_start > time_of_inquiry_obj:
                print(
                    f"\033[91mPackage ID: {package_id}, Address: {table.lookup(package_id)[0]}, {table.lookup(package_id)[1]}, {table.lookup(package_id)[2]}, weight: {table.lookup(package_id)[4]}, delivery deadline: {table.lookup(package_id)[3]} is at the hub.\033[0m")
            if delivery_start < time_of_inquiry_obj:
                if delivery_end < time_of_inquiry_obj:
                    print(
                        f"\033[32mPackage ID: {package_id}, Address: {table.lookup(package_id)[0]}, {table.lookup(package_id)[1]}, {table.lookup(package_id)[2]}, weight: {table.lookup(package_id)[4]}, delivery deadline: {table.lookup(package_id)[3]} was {table.lookup(package_id)[5]} at {table.lookup(package_id)[6]}.\033[0m")
                else:
                    print(
                        f"\033[33mPackage ID: {package_id}, Address: {table.lookup(package_id)[0]}, {table.lookup(package_id)[1]}, {table.lookup(package_id)[2]}, weight: {table.lookup(package_id)[4]}, delivery deadline: {table.lookup(package_id)[3]} is en route.\033[0m")
    if user_input == 3:
        time_of_inquiry = input("Enter the time in military time, i.e., 0900: ")
        time_of_inquiry_obj = datetime.strptime(time_of_inquiry, '%H%M')

        for i in range(len(table.data_map)):
            if table.lookup(str(i)) is not None:
                delivery_start = datetime.strptime(table.lookup(str(i))[8], "%I:%M:%S %p")
                delivery_end = datetime.strptime(table.lookup(str(i))[6], "%I:%M:%S %p")
                if delivery_start > time_of_inquiry_obj:
                    print(
                        f"\033[91mPackage ID: {str(i)}, Address: {table.lookup(str(i))[0]}, {table.lookup(str(i))[1]}, {table.lookup(str(i))[2]}, weight: {table.lookup(str(i))[4]}, delivery deadline: {table.lookup(str(i))[3]} is at the hub.\033[0m")
                if delivery_start < time_of_inquiry_obj:
                    if delivery_end < time_of_inquiry_obj:
                        print(
                            f"\033[32mPackage ID: {str(i)}, Address: {table.lookup(str(i))[0]}, {table.lookup(str(i))[1]}, {table.lookup(str(i))[2]}, weight: {table.lookup(str(i))[4]}, delivery deadline: {table.lookup(str(i))[3]} was {table.lookup(str(i))[5]} at {table.lookup(str(i))[6]}.\033[0m")
                    else:
                        print(
                            f"\033[33mPackage ID: {str(i)}, Address: {table.lookup(str(i))[0]}, {table.lookup(str(i))[1]}, {table.lookup(str(i))[2]}, weight: {table.lookup(str(i))[4]}, delivery deadline: {table.lookup(str(i))[3]} is en route.\033[0m")

    if user_input == 4:
        print("Program Exiting")
        return


def delivered_between(time1: str, time2: str, table: HashTable):
    time_clean1 = datetime.strptime(time1, '%H%M')
    time_clean2 = datetime.strptime(time2, '%H%M')
    time_clean1_str = datetime.strftime(time_clean1, "%I:%M:%S %p")
    time_clean2_str = datetime.strftime(time_clean2, "%I:%M:%S %p")
    print()
    print(f"Status of all packages at a time between {time_clean1_str} and {time_clean2_str}")
    print()
    for i in range(1, len(table.data_map)):
        delivery_start = datetime.strptime(table.lookup(str(i))[8], "%I:%M:%S %p")
        delivery_end = datetime.strptime(table.lookup(str(i))[6], "%I:%M:%S %p")
        if delivery_start > time_clean1 and delivery_start > time_clean2:
            print(
                f"\033[91mPackage ID: {str(i)}, Address: {table.lookup(str(i))[0]}, {table.lookup(str(i))[1]}, {table.lookup(str(i))[2]}, weight: {table.lookup(str(i))[4]}, delivery deadline: {table.lookup(str(i))[3]} is at the hub.\033[0m")

        if (delivery_start < time_clean2 < delivery_end) or (
                time_clean1 < delivery_start < time_clean2):
            print(
                f"\033[33mPackage ID: {str(i)}, Address: {table.lookup(str(i))[0]}, {table.lookup(str(i))[1]}, {table.lookup(str(i))[2]}, weight: {table.lookup(str(i))[4]}, delivery deadline: {table.lookup(str(i))[3]} is en route.\033[0m")

        if delivery_start < time_clean1 and delivery_end < time_clean2:
            print(
                f"\033[32mPackage ID: {str(i)}, Address: {table.lookup(str(i))[0]}, {table.lookup(str(i))[1]}, {table.lookup(str(i))[2]}, weight: {table.lookup(str(i))[4]}, delivery deadline: {table.lookup(str(i))[3]} was {table.lookup(str(i))[5]} at {table.lookup(str(i))[6]}.\033[0m")
