# The Node class has two methods. The init and add_child are two methods.
# You know that init method is a constructor, and it executes when you call a class (Here is Node) default.

# The child nodes you are maintaining in a list. That’s you can see in the init method.
# The add_child methods takes input and create a list of child nodes.

class Node():
    def __init__(self, val):
        self.val = val
        self.child = []

    def add_child(self, node):
        self.child.append(node)

# step 1
root = Node(1)
print(root)

# step 2
print(root.child)

# step 3
child1 = Node(2)
child2 = Node(3)
child3 = Node(4)
root.add_child(child1)
root.add_child(child2)
root.add_child(child3)
print(root.child)

# step 4
print(root.val)
for c in root.child:
    print(c.val)