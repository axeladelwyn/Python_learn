# Problem Set 4A
# Name: Axel
# Collaborators:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10)) #TODO
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10))) #TODO
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26)))) #TODO

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # TODO: Remove pass and write your code here
    # iF tea if a leaf, it has a height of 0
    # Recursive case Find the height of T left and right and take the maximum mof the two
    # add 1 to the maximum and return it
    if tree is None:
        return -1
    else:
        left_height = find_tree_height(tree.left)
        right_height = find_tree_height(tree.right)
        return max(left_height,right_height) + 1


def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    # TODO: Remove pass and write your code here
    if tree is None:
        return True

    if tree.left is not None:
        if not compare_func(tree.left.value, tree.value):
            return False
        if not is_heap(tree.left, compare_func):
            return False

    if tree.right is not None:
        if not compare_func(tree.right.value, tree.value):
            return False
        if not is_heap(tree.right, compare_func):
            return False
    return True

def max_heap_compare(child_value, parent_value):
    if child_value < parent_value:
        return True
    return False
def min_heap_compare(child_value, parent_value):
    if child_value > parent_value:
        return True    
    return False



if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    print(is_heap(tree1, max_heap_compare))  
    print(is_heap(tree2, max_heap_compare))
