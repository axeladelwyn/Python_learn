def remove_and_sort(Lin, k):
    """ Lin is a list of ints
        k is an int >= 0
    Mutates Lin to remove the first k elements in Lin and 
    then sorts the remaining elements in ascending order.
    If you run out of items to remove, Lin is mutated to an empty list.
    Does not return anything.
    """
    # Your code here  
    # remove the first k element in lin using remove or pop?
    # sort the List using sort() method
    # If we remove all of things it becomes empty list
    if k >= len(Lin):
        Lin.clear()
    else:
        del Lin[:k] 

    Lin.sort()

# Examples:
L = [1,6,3]
k = 1
remove_and_sort(L, k)
print(L)   # prints the list [3, 6]