# Team 6 - Liam Hennessy, Anna Zheng
# PID: Liam - 5499630, Anna - 4397893
# Submission Date: Nov 8, 2022
# This returns the next value of the current node in a preorder tree traversal


# Initialize the node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Preorder traversal and print the data
def preorder_next(root: Node, key: Node):

    # sanity check for the root to exist
    if root is None:
      return
    
    # setting up a stack to add nodes to
    stack = []
    stack.append(root)
    key_found = False       

    # looping through until the stack is empty
    while(len(stack) > 0):
      node = stack.pop()

      if key_found:
        return node.data
    
      # if our current node is the same as the key node we
      # set `key_found` to true 
      # so that we can return the next node's data
      if node == key:
        key_found = True

    # adding the nodes to the stack
      if node.right is not None:
        stack.append(node.right)
        
      if node.left is not None:
        stack.append(node.left)

# Driver code
if __name__ == "__main__":
    print("Building the sample#1 binary tree with pre-order traversal:")
    root = Node(1)
    root.left = Node(2)  # type: ignore
    root.right = Node(3)  # type: ignore
    root.left.left = Node(4)  # type: ignore
    root.left.right = Node(5)  # type: ignore
    print(preorder_next(root, root))
    print(preorder_next(root, root.left))
    print(preorder_next(root, root.left.left))
    print(preorder_next(root, root.left.right))
    # 3 is the last node; therefore, we do not give it as input.

    print("Building the sample#2 binary tree with pre-order traversal:")
    root = Node(1)
    root.left = Node(2)   # type: ignore
    root.right = Node(5)  # type: ignore
    root.left.left = Node(3)  # type: ignore
    root.left.right = Node(4)  # type: ignore
    root.right.left = Node(6)  # type: ignore
    root.right.right = Node(7)  # type: ignore
    print(preorder_next(root, root))
    print(preorder_next(root, root.left))
    print(preorder_next(root, root.left.left))
    print(preorder_next(root, root.left.right))
    print(preorder_next(root, root.right))
    print(preorder_next(root, root.right.left))
    # # 7 is the last node; therefore, we do not give it as input.