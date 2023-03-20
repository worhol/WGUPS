from datetime import datetime
from HashTable import HashTable


# This function takes the HashTable object as the argument and then displays options for user to interact with a
# package delivery system. If user chooses option 1, application prints out status for all packages and prints a
# total mileage all trucks covered during a delivery. If user choose option 2, application prompts the user to enter
# the unique id for the package and the time that user wants to check the status of the package. It then prints out
# the status of the package at inquired time. If user choose option 3, application prompts user to enter the time. It
# then prints out the statuses of all packages at given time.
# If user choose option 4, application ends execution with a message "Program Exiting".
def menu(table: HashTable):
    # Prints the prompt
    print("1. Print All Package Status and Total Mileage\n2. Get a Single Package Status with a "
          "Time\n3."
          "Get All Package Status with a Time\n4. Exit the Program")
    # Takes user input and sets it as integer in user_input variable
    user_input = int(input("Enter your choice:"))
    # Checks the user input and create the mileage list to store the mileages from each package
    if user_input == 1:
        mileage = []
        # Runs the loop in HashTable object and by calling the lookup function searches for the value corresponding
        # with a stored mileage for each package. It then adds the value to the mileage list.
        for i in range(1, len(table.data_map)):
            mileage.append(table.lookup(str(i))[7])
            # Prints the status report for each package
            print(
                f"Package ID: {str(i)}, Address: {table.lookup(str(i))[0]}, {table.lookup(str(i))[1]}, {table.lookup(str(i))[2]}, weight: {table.lookup(str(i))[4]}, delivery deadline: {table.lookup(str(i))[3]} was {table.lookup(str(i))[5]} at {table.lookup(str(i))[6]}.")
        print()
        # Each package contains mileage float value which is combined value of all mileages of the
        # individual packages delivered by the individual truck. Since those are the three distinct values,
        # the set function filters three unique values and then the sum function sums them up.
        # The application then prints the sum as a total mileage.
        print(f"TOTAL MILEAGE IS: {sum(set(mileage))}")

    # Checks the user input
    if user_input == 2:
        # Prompts the user to enter the package id and stores it package_id variable as a string
        package_id = str(input("Please enter the package ID: "))
        # Prompts the user to enter the time and stores it in the time_of_inquiry variable
        time_of_inquiry = input("Enter the time in military time, i.e., 0900: ")
        # Creates the datetime object with time_of_inquiry
        time_of_inquiry_obj = datetime.strptime(time_of_inquiry, '%H%M')
        # Calls the HashTable function lookup to check if the id is stored as a key in the table
        if table.lookup(package_id) is not None:
            # Creates a datetime object delivery_start which is stored as a string for each package at the beginning
            # of the delivery.
            delivery_start = datetime.strptime(table.lookup(package_id)[8], "%I:%M:%S %p")
            # Creates a datetime object delivery_end which is stored as a string for each package at the end
            # of the delivery.
            delivery_end = datetime.strptime(table.lookup(package_id)[6], "%I:%M:%S %p")
            # Checks if the delivery started after the inquiry time, then prints the status of the package which is
            # "at the hub".
            if delivery_start > time_of_inquiry_obj:
                print(
                    f"Package ID: {package_id}, Address: {table.lookup(package_id)[0]}, {table.lookup(package_id)[1]}, {table.lookup(package_id)[2]}, weight: {table.lookup(package_id)[4]}, delivery deadline: {table.lookup(package_id)[3]} is at the hub.")
            # Checks if the delivery started before or at the time of inquiry
            if delivery_start <= time_of_inquiry_obj:
                # If the delivery ended before or at the time of the inquiry prints the package's status
                # as delivered at the time of the delivery.
                if delivery_end <= time_of_inquiry_obj:
                    print(
                        f"\033[32mPackage ID: {package_id}, Address: {table.lookup(package_id)[0]}, {table.lookup(package_id)[1]}, {table.lookup(package_id)[2]}, weight: {table.lookup(package_id)[4]}, delivery deadline: {table.lookup(package_id)[3]} was {table.lookup(package_id)[5]} at {table.lookup(package_id)[6]}.\033[0m")
                # If the delivery ended after the time of the inquiry prints the package's status
                # as "en route".
                else:
                    print(
                        f"\033[33mPackage ID: {package_id}, Address: {table.lookup(package_id)[0]}, {table.lookup(package_id)[1]}, {table.lookup(package_id)[2]}, weight: {table.lookup(package_id)[4]}, delivery deadline: {table.lookup(package_id)[3]} is en route.\033[0m")
    # Checks the user input
    if user_input == 3:
        # Prompts the user to enter the time and stores it in the time_of_inquiry variable
        time_of_inquiry = input("Enter the time in military time, i.e., 0900: ")
        # Creates the datetime object with time_of_inquiry
        time_of_inquiry_obj = datetime.strptime(time_of_inquiry, '%H%M')
        # Enters the loop through all packages stored in the HashTable object
        for i in range(len(table.data_map)):
            # Checks if each key is in the table
            if table.lookup(str(i)) is not None:
                # Creates a datetime object delivery_start which is stored as a string for each package at the beginning
                # of the delivery.
                delivery_start = datetime.strptime(table.lookup(str(i))[8], "%I:%M:%S %p")
                # Creates a datetime object delivery_end which is stored as a string for each package at the end
                # of the delivery.
                delivery_end = datetime.strptime(table.lookup(str(i))[6], "%I:%M:%S %p")
                # Checks if the start of the delivery was after the time of the inquiry, then prints out the delivery
                # status for that package as "at the hub"
                if delivery_start > time_of_inquiry_obj:
                    print(
                        f"Package ID: {str(i)}, Address: {table.lookup(str(i))[0]}, {table.lookup(str(i))[1]}, {table.lookup(str(i))[2]}, weight: {table.lookup(str(i))[4]}, delivery deadline: {table.lookup(str(i))[3]} is at the hub.")
                # Checks if the delivery started before or at the time of inquiry
                if delivery_start <= time_of_inquiry_obj:
                    # If the delivery ended before or at the time of the inquiry prints the package's status
                    # as delivered at the time of the delivery.
                    if delivery_end <= time_of_inquiry_obj:
                        print(
                            f"\033[32mPackage ID: {str(i)}, Address: {table.lookup(str(i))[0]}, {table.lookup(str(i))[1]}, {table.lookup(str(i))[2]}, weight: {table.lookup(str(i))[4]}, delivery deadline: {table.lookup(str(i))[3]} was {table.lookup(str(i))[5]} at {table.lookup(str(i))[6]}.\033[0m")
                    # If the delivery ended after the time of the inquiry prints the package's status
                    # as "en route".
                    else:
                        print(
                            f"\033[33mPackage ID: {str(i)}, Address: {table.lookup(str(i))[0]}, {table.lookup(str(i))[1]}, {table.lookup(str(i))[2]}, weight: {table.lookup(str(i))[4]}, delivery deadline: {table.lookup(str(i))[3]} is en route.\033[0m")
    # Checks the user input
    if user_input == 4:
        # Exits the program
        print("Program Exiting")
        return


# This function takes the two strings representing time and a HashTable object as arguments. It then returns the
# status of all packages between the two given times.
def delivered_between(time1: str, time2: str, table: HashTable):
    # Creates a datetime object from the argument string
    time_clean1 = datetime.strptime(time1, '%H%M')
    # Creates a datetime object from the argument string
    time_clean2 = datetime.strptime(time2, '%H%M')
    # Formats the datetime objects into desired string
    time_clean1_str = datetime.strftime(time_clean1, "%I:%M:%S %p")
    # Formats the datetime objects into desired string
    time_clean2_str = datetime.strftime(time_clean2, "%I:%M:%S %p")
    print()
    print(f"Status of all packages at a time between {time_clean1_str} and {time_clean2_str}")
    print()
    # Enters the loop through all packages stored in the HashTable object
    for i in range(1, len(table.data_map)):
        # Creates a datetime object delivery_start which is stored as a string for each package at the beginning
        # of the delivery.
        delivery_start = datetime.strptime(table.lookup(str(i))[8], "%I:%M:%S %p")
        # Creates a datetime object delivery_end which is stored as a string for each package at the end
        # of the delivery.
        delivery_end = datetime.strptime(table.lookup(str(i))[6], "%I:%M:%S %p")
        # Checks if the delivery started after the inquired time frame, then prints out the delivery
        # status for that package as "at the hub"
        if delivery_start > time_clean1 and delivery_start > time_clean2:
            print(
                f"Package ID: {str(i)}, Address: {table.lookup(str(i))[0]}, {table.lookup(str(i))[1]}, {table.lookup(str(i))[2]}, weight: {table.lookup(str(i))[4]}, delivery deadline: {table.lookup(str(i))[3]} is at the hub.")
        # Checks if the delivery started after or at the upper time constraint and delivery ended after the upper
        # time constraint, or delivery started after  or at the lower time constraint and before the upper
        # time constraint then prints the status of the package as "en route"
        if (delivery_start <= time_clean2 < delivery_end) or (
                time_clean1 <= delivery_start <= time_clean2):
            print(
                f"\033[33mPackage ID: {str(i)}, Address: {table.lookup(str(i))[0]}, {table.lookup(str(i))[1]}, {table.lookup(str(i))[2]}, weight: {table.lookup(str(i))[4]}, delivery deadline: {table.lookup(str(i))[3]} is en route.\033[0m")
        # Checks if delivery started before the lower time constraint and that delivery ended before the upper time
        # constraint, then prints the status of the package as "delivered" at the time of the delivery
        if delivery_start <= time_clean1 and delivery_end <= time_clean2:
            print(
                f"\033[32mPackage ID: {str(i)}, Address: {table.lookup(str(i))[0]}, {table.lookup(str(i))[1]}, {table.lookup(str(i))[2]}, weight: {table.lookup(str(i))[4]}, delivery deadline: {table.lookup(str(i))[3]} was {table.lookup(str(i))[5]} at {table.lookup(str(i))[6]}.\033[0m")
