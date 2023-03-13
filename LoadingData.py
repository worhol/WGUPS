from HashTable import HashTable
from Package import Package


def load_package_data(table: HashTable):
    info = []
    with open("packageCSV.csv", encoding='utf-8-sig') as file:
        for line in file:
            info.append(line.strip())
        for i in info:
            parts = i.split(",")
            package = Package(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], "at the hub", parts[6],
                              parts[7],None,0.0, None)
            table.insert(package.id, [package.address, package.city, package.zip, package.delivery_time,
                                      package.weight, package.status, package.delivered_at, package.mileage, package.start_time])


def load_distance_data(data: list):
    with open("distanceCSV.csv", encoding='utf-8-sig') as file:
        for line in file:
            row = line.strip().split(",")
            while '' in row:
                i = row.index('')
                row.pop(i)
            row = [float(i) for i in row]
            data.append(row)


def load_address_data(data: list):
    with open("addressCSV.csv", encoding='utf-8-sig') as file:
        temp = []
        for line in file:
            line.rstrip(" ")
            temp.append(line.strip())

        for i in temp:
            parts = i.split(",")
            data.append(parts)
