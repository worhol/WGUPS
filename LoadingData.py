from HashTable import HashTable
from Package import Package


# This function takes the HashTable object as the argument, process the csv. file then creates the package object
# from the content of the file then inserts the package object into a HashTable object

def load_package_data(table: HashTable):
    # Creates empty list info
    info = []
    # Opens the csv file
    with open("packageCSV.csv", encoding='utf-8-sig') as file:
        # Loops through each line of the file
        for line in file:
            # Removes special character at the end of the line and adds each line of the file to the info list
            info.append(line.strip())
        # Loops through the info list
        for i in info:
            # Splits the item in the list based on the commas
            parts = i.split(",")
            # Creates the package object with the values from the parts
            package = Package(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], "at the hub", parts[6],
                              parts[7], None, 0.0, None)
            # Inserts the package object values as the value into the HashTable object and assign the key to that
            # value as the package ID.
            table.insert(package.id, [package.address, package.city, package.zip, package.delivery_time,
                                      package.weight, package.status, package.delivered_at, package.mileage,
                                      package.start_time])


# This function takes the list as the argument, process the csv file then adds the processed data to the argument list
def load_distance_data(data: list):
    # Opens the csv file
    with open("distanceCSV.csv", encoding='utf-8-sig') as file:
        # Loops through the line of the file
        for line in file:
            # Splits the content of each line by commas and removes the special characters at the end of the line
            row = line.strip().split(",")
            # Loops through each row and removes the empty space
            while '' in row:
                i = row.index('')
                row.pop(i)
            # For each element in a row appends it as a float to a new list
            row = [float(i) for i in row]
            # Each row gets added to a list object taken as an argument
            data.append(row)

# This function takes the list as the argument, process the csv file then adds the processed data to the argument list
def load_address_data(data: list):
    # Opens the csv file
    with open("addressCSV.csv", encoding='utf-8-sig') as file:
        # Creates the empty list
        temp = []
        # Loops through each file
        for line in file:
            # Cleans each line in a file from empty string on its right
            line.rstrip(" ")
            # Adds each line to the temp list. Strips the line again from special characters
            temp.append(line.strip())
        # Loops through  each element in a list
        for i in temp:
            # Splitting each element by commas
            parts = i.split(",")
            # Adds each part to the list taken as a argument
            data.append(parts)
