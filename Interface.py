from datetime import datetime
from HashTable import HashTable


def menu( table: HashTable):


    print("1. Print All Package Status and Total Mileage\n2. Get a Single Package Status with a "
                           "Time\n3."
                     "Get All Package Status with a Time\n4. Exit the Program")
    user_input = int(input("Enter your choice:"))
    if user_input==2:
        time=input("Enter the time in military time, i.e., 0900 :")
        time_converted=datetime.strptime(time,"%I:%M %p")

        print(table.lookup(str(package_number)))
