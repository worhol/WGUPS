class HashTable:
    # This method initialize the map data_map by creating a list with a 41 items in it that will contain None
    def __init__(self, size=41):
        self.data_map = [None] * size

    # This method takes a key and returns the address where to store the key, value pair
    def __hash(self, key):
        # Variable my_hash is initialized to 0
        my_hash = 0
        # Enters the loop through the letters of the key given as the argument
        for i in key:
            # adds ASCII value of the letter represented an integer given by the ord() function multiplied by the
            # prime number 23, then it takes the reminder of that sum divided by the length of the data_map and
            # assign the result to my_hash variable
            my_hash = (my_hash + ord(i) * 23) % len(self.data_map)
        return my_hash

    # This method prints the HashTable
    def print_table(self):
        # Loops through the data_map
        for i, val in enumerate(self.data_map):
            # Prints key, value pair
            print(i, ":", val)

    # This method takes the key and value as the arguments and inserts the key, value pair into the list
    def insert(self, key, value):
        # Create a variable index and assign it a hashed value of the key argument
        index = self.__hash(key)
        # Check if there is no empty list at the address
        if self.data_map[index] is None:
            # Initialize the empty list in the map with the index value as the address
            self.data_map[index] = []
            # Add the key, value pair to the newly created list
        self.data_map[index].append([key, value])

    # This method takes the key value as the argument and returns the value associated with a key
    def lookup(self, key):
        # Create a variable index and assign it a hashed value of the key argument
        index = self.__hash(key)
        # Checks that data_map at the index is not None
        if self.data_map[index] is not None:
            # Loops through the index address in the data_map
            for i in range(len(self.data_map[index])):
                # Checks if the key given as the argument matches the key  at address
                if self.data_map[index][i][0] == key:
                    # returns the value associated with a key
                    return self.data_map[index][i][1]
        # If the key was not found in the HashTable returns None
        return None
