class Node:

	# Function to initialize the node object
	def __init__(self, data):
		self.data = data  # Assign data
		self.next = None  # Initialize next as null


class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new node at the beginning
	def push(self, new_data):

		# 1  & 2: Allocate the Node & put in the data
		new_node = Node(new_data)

		# 3. Make next of new Node as head
		new_node.next = self.head

		# 4. Move the head to point to the Node
		self.head = new_node

	# Inserts a new node after the given prev_node
	def insertAfter(self, prev_node, new_data):

		# 1 Check if the give prev_node exists
		if prev_node is None:
			print("The given previous node must be in LinkedList.")
			return

		# 2 Create new node & 3 put in the data
		new_node = Node(new_data)

		# 4 Make next of new Node as next of prev_node
		new_node.next = prev_node.next

		# 5 make next of prev_node as new_node
		prev_node.next = new_node

	# Utility function to print the linked list

	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data, end=' ')
			temp = temp.next

# Code execution starts here

if __name__ == '__main__':
	# Start with the empty list
	llist = LinkedList()

	# Insert 6 so linked list becomes 6->None
	llist.push(6)

	# Insert 7 at the beginning. so llist become 7->6->None
	llist.push(7)

	# insert 1 at the beginning
	llist.push(1)

	# insert 4 at the beginning
	llist.push(4)

	# insert8, after 7. so linked list become 4->1->8->7->6->None
	llist.insertAfter(llist.head.next, 8)

	print("Created singly linked list is:")
	llist.printList()
