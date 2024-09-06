def flatten(L):
    """ 
    L: a list 
    Returns a copy of L, which is a flattened version of L 
    """
    # Your code here  
    if L == []:
        return L
    if isinstance(L[0], list):
        return flatten(L[0]) + flatten(L[1:])

    return [L[0]] + flatten(L[1:])
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]