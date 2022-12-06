# Team 6 - Liam Hennessy, Anna Zheng
# PID: Liam - 5499630, Anna - 4397893
# Submission Date: Dec 1, 2022

class HashTable():
    def __init__(self):
        # Input for size
        # Initialize list
        self.n = input("Enter the size of the Hash Table: ")
        self.list = [0 for i in range(int(self.n))]

    def insert(self, val):
        # Initializing probing value
        count = 0
        # Flag for only print collision output once.
        flag = False
        # Get hash position with linear probing calculation.
        hash_position = (val + count) % int(self.n)

        while self.list[hash_position] != 0:
            if flag == False:
                print("Collision has occurred for element "+str(val)+" at position "+str(hash_position)+". Finding new Position.")
                flag = True
            # Increment probing value
            count += 1
            # Get new hash position with updated probing value.
            hash_position = (val + count) % int(self.n)

            # Only print the value that didn't go through collision
        if flag == False:
            print("Element "+str(val)+" at position "+str(hash_position))
        # Insert value at hash position.
        self.list[hash_position] = val

    def insert_test(self, val):
        # -------------------------------------------------------------------------
        # -------------- This code will print all collision position --------------
        # --------------            Limited by list size             --------------
        # -------------------------------------------------------------------------

        # Loop through each index of the table
        for j in range(int(self.n)):
            # Linear probing hash position
            hash_position = (val + j) % int(self.n)
            # If hash position is taken
            # print collision output
            if self.list[hash_position] != 0:
                print("Collision has occurred for element "+str(val)+" at position "+str(hash_position)+". Finding new Position.")
                continue
            # Else, insert value into table
            # and exit loop
            else:
                self.list[hash_position] = val
                break
        # Print inserted position
        print("Element "+str(val)+" at position " + str(hash_position)) # type: ignore

    def display(self):
        print("Displaying the table...")
        # Number of element in table
        count = 0
        # Loop through the table and print out the index and value.
        for k in range(int(self.n)):
            print(str(k) + " = " + str(self.list[k]))
            # If index has a value then increment count.
            if int(self.list[k]) != 0:
                count += 1
        # Print the final count.
        print("The number of elements in the Table are: "+ str(count))


# Driver Code
table1 = HashTable()

# storing elements in table
table1.insert(12)
table1.insert(26)
table1.insert(31)
table1.insert(17)
table1.insert(90)
table1.insert(28)
table1.insert(88)
table1.insert(40)
table1.insert(77)

# displaying the Table
table1.display()




