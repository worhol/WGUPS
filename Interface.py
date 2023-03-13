from datetime import datetime
from HashTable import HashTable


def menu(table: HashTable):
    print("1. Print All Package Status and Total Mileage\n2. Get a Single Package Status with a "
          "Time\n3."
          "Get All Package Status with a Time\n4. Exit the Program")
    user_input = int(input("Enter your choice:"))
    if user_input == 1:
        mileage = []
        for i in range(1,len(table.data_map)):
            mileage.append(table.lookup(str(i))[7])
            print(f"Package ID: {i}, {table.lookup(str(i))}")
        print()
        print(f"TOTAL MILEAGE IS: {sum(set(mileage))}")
    if user_input == 2:
        time_str = input("Enter the time in military time, i.e., 0900: ")
        time_obj = datetime.strptime(time_str, '%H%M')
        # formatted_time = time_obj.strftime('%I:%M %p')

        for i in range(len(table.data_map)):
            if table.lookup(str(i)) is not None:
                package_status = table.lookup(str(i))[5]
                delivery_time_str = table.lookup(str(i))[6]

                if delivery_time_str is None:
                    if package_status == "at the hub":
                        print(f"\033[91mPackage ID: {i}, Address: {table.lookup(str(i))[0]} {package_status}\033[0m")
                    # else:
                    #     print(f"Package {i}: en route")
                else:
                    delivery_time_obj = datetime.strptime(delivery_time_str, '%I:%M:%S %p')
                    if delivery_time_obj.time() <= time_obj.time():
                        print(f"\033[32mPackage ID: {i}, Address: {table.lookup(str(i))[0]} {package_status} at {table.lookup(str(i))[6]}\033[0m")
                    else:
                        print(f"\033[33mPackage ID: {i}, Address: {table.lookup(str(i))[0]} en route \033[0m")

    if user_input == 3:

        package_id = str(input("Please enter the package ID: "))
        time_of_inquiry=input("Enter the time in military time, i.e., 0900: ")
        time_obj = datetime.strptime(time_of_inquiry, '%H%M')
        if table.lookup(package_id) is not None:
            package_status = table.lookup(package_id)[5]
            delivery_time_str = table.lookup(package_id)[6]

            if delivery_time_str is None:
                if package_status == "at the hub":
                    print(f"\033[91mPackage ID: {package_id}, Address: {table.lookup(package_id)[0]} {package_status}\033[0m")
                # else:
                #     print(f"Package {i}: en route")
            else:
                delivery_time_obj = datetime.strptime(delivery_time_str, '%I:%M:%S %p')
                if delivery_time_obj.time() <= time_obj.time():
                    print(
                        f"\033[32mPackage ID: {package_id}, Address: {table.lookup(package_id)[0]} {package_status} at {table.lookup(package_id)[6]}\033[0m")
                else:
                    print(f"\033[33mPackage ID: {package_id}, Address: {table.lookup(package_id)[0]} en route \033[0m")

    if user_input == 4:
        print("Program Exiting")
        return
