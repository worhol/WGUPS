from datetime import datetime
from HashTable import HashTable


def menu(table: HashTable):
    print("1. Print All Package Status and Total Mileage\n2. Get a Single Package Status with a "
          "Time\n3."
          "Get All Package Status with a Time\n4. Exit the Program")
    user_input = int(input("Enter your choice:"))
    if user_input == 2:
        time_str = input("Enter the time in military time, i.e., 0900: ")
        time_obj = datetime.strptime(time_str, '%H%M')
        formatted_time = time_obj.strftime('%I:%M %p')

        for i in range(len(table.data_map)):
            if table.lookup(str(i)) is not None:
                package_status = table.lookup(str(i))[5]
                delivery_time_str = table.lookup(str(i))[6]

                if delivery_time_str is None:
                    if package_status == "at the hub":
                        print(f"Package {i}: \033[91m{package_status}\033[0m")
                    # else:
                    #     print(f"Package {i}: en route")
                else:
                    delivery_time_obj = datetime.strptime(delivery_time_str, '%I:%M:%S %p')
                    if delivery_time_obj.time() <= time_obj.time():
                        # print(f"Package {i}: {package_status}")
                        print(f"\033[32mPackage {i}: {package_status}\033[0m")
                    else:
                        print(f"\033[33mPackage {i}: en route\033[0m")

    #     time = input("Enter the time in military time, i.e., 0900 :")
    #     time_obj = datetime.strptime(time, '%H%M')
    #     formatted_time = time_obj.strftime('%I:%M %p')
    # for i in range(len(table.data_map)):
    #     if table.lookup(str(i)) is not None:
    #         # if table.lookup(str(i))[5] =="at the hub":
    #         #     print("at hub")
    #         # if table.lookup(str(i))[6] > formatted_time:
    #         #     print(table.lookup(str(i))[5])
    #         #     if table.lookup(str(i))[5]!="delivered":
    #         #         print("en route")
    #         # if table.lookup(str(i))[6] is None:
    #         #     print (table.lookup(str(i)))
    #         if table.lookup(str(i))[6] is None:
    #             print (table.lookup(str(i))[5])
    #         if table.lookup(str(i))[6] is not None:
    #             if table.lookup(str(i))[6] < formatted_time:
    #                 print(table.lookup(str(i))[5])
    #             else:
    #                 print(table.lookup(str(i))[5])



        # print(table.lookup(str(i)))
