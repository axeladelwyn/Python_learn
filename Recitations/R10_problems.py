#############################################################################
# Problem 1:
# For each of the following expressions, what is the order of growth class 
# that best describes it?
# a) 8n   theta(n)
# b) 3n**2 + 7n**3 + 4 theta(n**3)   
# c) 5log(n) + 5n theta(n)
# d) 3**n + n**2  theta(n**2)
# e) 20n + nlog(n) theta(n)
# f) 5 + 60  constant
# g) log(n) + 4n theta(n)




#############################################################################
# Problem 2:
# Rank the following functions by runtime complexity. Note some may have 
# the same runtime complexity.

# f(n) = n**2 + 4n + 2
# g(n) = log(n**2)  theta(log n)
# h(n) = log2(n)  (i.e. read as log base 2 n) theta(log n)
# j(n) = 3n**3 + 2 Theta(n**3)
# l(n) = n! Theta(n!)
# k(n) = 2**n Theta(2**n)




#############################################################################
# Problem 3:
# What is the time complexity for the following programs? 

def program1():
    my_list = [1,2,3,4,5,6,7,8]
    my_list_even= []
    for i in range(len(my_list)):
        if i % 2 == 0:
            my_list_even.append(i)
    return my_list
#Theta(n)

def program2():
    my_list = [1,2,3,4,5,7]
    my_second_list = [1,2,3,4,5,7]
    
    output_list1 = [i for i in my_list]

    output_list2 = []
    for i in my_list: #first loop
        for j in my_second_list: # second loop
            output_list2 += [i,j]
    
    return (output_list1, output_list2)
#Theta(n^2)

def program3(n):
    epsilon = 0.01
    low = 0
    high = n
    ans = (high + low) / 2 
    
    while abs(ans**4 - n) >= epsilon:
        if ans**4 > n:
            high = ans 
        else: 
            low = ans
        ans = (high + low) / 2
    return ans

#theta log(n)


#############################################################################
# Problem 4:
# Describe two ways to construct an algorithm to find the maximum number is a list. 
# One algorithm should have time complexity O(n), the other O(n**2). (Note the 
# O(n**2) algorithm is highly inefficient and we'd never actually use it 
# in practice).


def find_max_linear(L):
    if not L:
        return None
    max = L[0]
    for element in L:
        if element > max:
            max = element
    return max

def find_max_quadratic(L):
    """
    Finds the maximum number in a list using a quadratic search.
    
    Parameters:
    L (list): The list of numbers.
    
    Returns:
    int/float: The maximum number in the list.
    """
    if not L:
        return None  # Handle empty list case
    
    for i in range(len(L)):
        is_max = True
        for j in range(len(L)):
            if L[j] > L[i]:
                is_max = False
                break
        if is_max:
            return L[i]

# Example usage:
L = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(find_max_quadratic(L))  # Output: 9
