def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    # Your code here
    #tA returns the length of the tuple
    length = len(tA)
    product_two_tuples = tuple(element1 * element2 for element1, element2 in zip(tA,tB))
    product = sum(product_two_tuples)
    return (length, product)

# Examples:
tA = (1, 2, 3, 3, 4, 5, 7)
tB = (4, 5, 6, 2, 5)   
print(dot_product(tA, tB)) # prints (3,32)