# a function that add the numbers of a list together

def add_numbers(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

# a function that traverses a tree inn preorder 

def preorder(tree):  # type: ignore
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())  # type: ignore
        preorder(tree.get_right_child())  # type: ignore

# function returns the value of the node after we visit the value (key) of another node in a preorder traversal

def preorder(tree, key):
    if tree:
        if tree.get_root_val() == key:
            return tree.get_root_val()
        preorder(tree.get_left_child(), key)
        preorder(tree.get_right_child(), key)
