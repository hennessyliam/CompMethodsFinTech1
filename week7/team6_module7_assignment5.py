# Initialize the Node
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None


# Class for doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
        self.end_node = None

    # Insert Element to Empty list
    def insert_to_empty_list(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is empty")

    # Insert element at the end
    def insert_to_end(self, data):
        # Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    # Delete the elements from the start
    def delete_at_start(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_node.prev = None

    # Delete the elements from the end
    def delete_at_end(self):
        if self.start_node is None:
            if self.start_node.next is None:
                self.start_node = None
            else:
                temp = self.head
                while temp.next.next is not None:
                    temp = temp.next
                end_node = temp.next
                temp.next = None
                end_node = None

    def insert_at_index(self, new_element, index):
        new_node = Node(new_element)

        if index == 1:
            new_node.next = self.start_node 
            self.start_node.prev = new_node  
            self.start_node = new_node
        else:
            temp = self.start_node

            for i in range(1, index-1):
                if temp is not None:
                    temp = temp.next
            if temp is not None:
                new_node.next = temp.next
                new_node.prev = temp
                temp.next = new_node
                if new_node.next is not None:
                    new_node.next.prev = new_node
            else:
                print("The previous node is null.")

    def display(self):
        temp = self.start_node
        if temp is not None:
            print(end="")
            while temp is not None:
                print(temp.item)
                temp = temp.next
            print()
        else:
            print("The list is empty.")


# Driver Code:
# Create a new Doubly Linked List
dll = DoublyLinkedList()
# Display Data
dll.display()
# Insert the element to empty list
dll.insert_to_empty_list(10)
# Insert the element at the end
dll.insert_to_end(20)
dll.insert_to_end(30)
dll.insert_to_end(40)
dll.insert_to_end(50)
dll.insert_to_end(60)
dll.insert_at_index(35, 3)
dll.insert_at_index(38, 4)
dll.insert_at_index(3, 0)
# Display Data
dll.display()
# Delete elements from start
dll.delete_at_start()
# Delete elements from end
dll.delete_at_end()
# Display Data
dll.display()
