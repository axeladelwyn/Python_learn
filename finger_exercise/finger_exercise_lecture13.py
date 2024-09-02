def sum_str_lengths(L):
    """
    L is a non-empty list containing either: 
    * string elements or 
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and 
    lengths of strings in the sublists of L. If L contains an 
    element that is not a string or a list, or L's sublists 
    contain an element that is not a string, raise a ValueError.
    """
    # Your code here  
    # we try to use list comprehension here
    # mutate the L ( change the L)
    total_length = 0
    Lnew = L[:]
    for item in Lnew:
        if isinstance(item, str):
            total_length += len(item)
        elif isinstance(item , list):
            total_length += sum_str_lengths(item)
        else:
            raise ValueError
    return total_length


# Examples:
print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
# print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
# print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError