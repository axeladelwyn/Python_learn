########################################################################
# Problem 1: List concatenation
original_list = [1,2,35,10,5,8,9,23]

# a) Using List concatenation create a new list from the orignal list, 
# removing all multiples of 5 from a list of numbers.
# expected output: [1, 2, 8, 9, 23]
# INSERT CODE HERE
def remove_multiple5(L):
    Lnew = L[:]
    new_list = []
    for elements in Lnew:
        # remove multiple of 5
        if elements % 5 != 0:
            new_list.append(elements)
    return new_list
print(remove_multiple5(original_list))

# b) Using list concatenation create a new list from the original list, 
# where each element is half the original element
# Expected output: [0.5, 1.0, 17.5, 5.0, 2.5, 4.0, 4.5, 11.5]
# INSERT CODE HERE
Lnew = original_list[:]
result = [x/2 for x in Lnew ]
print(result)

########################################################################
# Problem 2: Write a Function to insert a specified element x in a given list 
# after every nth element.
# Return the new list. 
# Example
# Original list:
# [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# Insert 20 in list after every 4th element:
# [1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]

def insert_element_list1(lst, x, n):
    """
    Parameters:
    lst: input list
    x: element to insert
    n: x will be inserted after every nth element
    Returns: new modified list 
    """
    # INSERT CODE HERE
    # append x  every n element
    reset_counter = 0
    Lnew = lst[:]
    i = n
    while i < len(Lnew):
        Lnew.insert(i,x)
        i += n + 1
    return Lnew
    
# testing
nums = [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
x = 20
n = 4
print(insert_element_list1(nums, x, n))


########################################################################
# Problem 3: Write a Function to sort list of lists containing integers such that the 
# sub-lists are sorted in increasing order. How would you sort in decreasing order?
print(f"#################PROBLEM3#####################")
# Example:
# Original list of tuples:
# [[10, 10.12, 10.11], [5, 5.3, 4.9], [2.4, 2.6, 2.2]]
# Expected output:
# [[10, 10.11, 10.12], [4.9, 5, 5.3], [2.2, 2.4, 2.6]]

def sort_list_of_lists(lst):
    """
    Parameters:
    lst: input list
    n: index to sort by
    Returns: the sorted list 
    """
    # INSERT CODE HERE
    # iterage through the list
    Lnew = lst[:]
    for i in range(len(Lnew)):
        Lnew[i] = sorted(Lnew[i])

    return Lnew # its the last element 

# testing
items = [[10, 10.12, 10.11], [5, 5.3, 4.9], [2.4, 2.6, 2.2]]
print(sort_list_of_lists(items))


########################################################################
# Problem 4: Write a Function to split a given list into size n chunks 
# using list comprehension. If the list does not divide equally, the last 
# chunk should be short. Return the new list. 

# Example:
# Original list:
# [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Split the list into equal size 4
# [[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]
# Split the list into equal size 5
# [[12, 45, 23, 67, 78], [90, 45, 32, 100, 76], [38, 62, 73, 29, 83]]
print("################# PROBLEM 4 ################")
def split_list(lst, n):
    """
    Parameters:
    lst: input list
    n: size of chunks
    Returns: new split list 
    """
    # INSERT CODE HERE
    num_chunks = (len(lst) + n - 1) // n
    print(num_chunks)
    chunks = [lst[i:i + n] for i in range(0, len(lst), n)]
    
    return chunks

# testing
nums = [12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
n = 4
print(split_list(nums,n))
n = 5
print(split_list(nums,n))
n = -1
print(split_list(nums, n))







