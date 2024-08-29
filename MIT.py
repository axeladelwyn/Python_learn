import string

def apply(criteria,n):
    """ criteria is a function that takes in a number and returns a Boolean
        n is an int
    Returns how many ints from 0 to n (inclusive) match the criteria 
    (i.e. return True when criteria is applied to them)
    """ 
    count = 0
    for i in range(1, n+1):
        if criteria(i):
            count += 1
    return count

def is_even(x):
    return x%2==0

def is_5(x):
    return x==5

# print('apply with is_5:',apply(is_5,10))
# print('apply with anon fcn:', apply(lambda x: x==5, 100))


# Shown another way, the following are equivalent:
is_even(8)              # returns True
(lambda x: x%2==0)(8)   # returns True


# 1. What does this print?
print(apply(lambda x: x%2==0, 10))

# 2. Call apply on n=100 and a lambda func 
#    that takes in a parameter and returns 
#    whether the parameter is a multiple of 10
#    What does it print?
# your code here
print(apply(lambda x: x%10==0, 100))

def do_twice(n, fn):
    return fn(fn(n))

print(do_twice(3, lambda x: x**2))
print(do_twice(3, lambda x: x**3))


###################
### example with returning a tuple with many values
###################
def quotient_and_remainder(x, y):
      q = x // y
      r = x % y
      return (q, r)

# result = quotient_and_remainder(10,3)
# print(result)

(quot, rem) = quotient_and_remainder(5,2)
print('quotient is:', quot)
print('remainder is:', rem)



############### YOU TRY IT #####################
# Write a function that meets these specifications:
def char_counts(s):
    """ s is a string of lowercase chars 
    Returns a tuple where the first value is the 
    number of vowels in s and the second value 
    is the number of consonants in s 
    """
    # your code here
    lower_alphabet = string.ascii_lowercase
    vowels = "aeiou"
    consonant = "bcdfghjklmnpqrstvwxyz"
    counter_vowel = 0
    counter_consonant = 0
    for char in s:
        if char not in vowels:
            counter_consonant += 1
        elif char in vowels:
            counter_vowel += 1
    return (counter_vowel,counter_consonant)

# print(char_counts("abcd"))  # prints (1,3)
# print(char_counts("zcght"))  # prints (0,5)

##################################################


###################
### example of variable number of arguments
###################
def mean(*args):
    """
    Assumes at least one argument and all arguments are numbers. 
    Returns the mean of the arguments.
    """
    tot = 0
    for a in args:
        tot += a
    return tot/len(args)

print(mean(1,2,3,4,5,6))
print(mean(6,0,9))

## Compare above code with this one:
# Note args vs *args and mean((6,0,9)) vs mean(6,0,9)
def mean(args):
    tot = 0
    for a in args:
        tot += a
    return tot/len(args)

print(mean((1,2,3,4,5,6)))
print(mean((6,0,9)))

##################
## EXAMPLE: sum element values in a list 
##################
def list_sum(L):
    total = 0 
    for e in L: 
    # 1, 3, 5
        total += e 
    return(total)

print(f"the sum of this list is {list_sum([1,3,5])}")


###################
## EXAMPLE: sum lengths of string elements
####################
def len_sum(L):
    total = 0 
    for s in L: 
        total += len(s) 
    return(total)

print(f" return the length of the list {len_sum(['ab', 'def', 'g'])}")


#################################################



################## YOU TRY IT ###################
def sum_and_prod(L):
    """ L is a list of numbers 
    Return a tuple where the first value is the 
    sum of all elements in L and the second value 
    is the product of all elements in L 
    """
    # your code here
    total, product = (0, 1)

    for sum in L:
    # 4, 6 , 2 ,5
        total += sum
        product *= sum
    # how to do product?
    # given the list of number
    # iterate through sum?

    return (total, product)

print(sum_and_prod([4,6,2,5]))   # prints (17, 240)





#############################################
################## ANSWERS TO YOU TRY IT ####################
#############################################
def char_counts(s):
    """ s is a string of lowercase chars 
    Returns a tuple where the first value is the 
    number of vowels in s and the second value 
    is the number of consonants in s 
    """
    vowels, cons = 0, 0
    for i in s:
        if i in "aeiou":
            vowels += 1
        else:
            cons += 1
    return (vowels, cons)

# print(char_counts("abcd"))  # prints (1,3)
# print(char_counts("zcght"))  # prints (0,5)


def sum_and_prod(L):
    """ L is a list of numbers 
    Return a tuple where the first value is the 
    sum of all elements in L and the second value 
    is the product of all elements in L 
    """
    s, p = 0, 1
    
    for i in L:
      s += i
      p *= i
    return (s, p)

# print(sum_and_prod([1,2,3,4]))   # prints (10, 24)
# print(sum_and_prod([12,6,2,7]))   # prints (27, 1008)


#############################################
################## AT HOME ####################
#############################################

# Trace this code:
# Figure out what it returns and then run it to check yourself.
def always_sunny(t1, t2):
    """ t1, t2 are non-empty """
    sun = ("sunny", "sun")
    first = t1[0] + t2[0]
    print(t1[0], t2[0])
    return (sun[0], first)

print(always_sunny(('cloudy'), ('cold',)))  # returns what?
# Because the comas in 'cold', is inside parentheses
# That means its counted as 1 tuple

print("##################################################")
def max_of_both(n, f1, f2):
    """ n is an int
        f1 and f2 are functions that take in an int and return a float
    Applies f1 and f2 on all numbers between 0 and n (inclusive). 
    Returns the maximum value of all these results.
    """
    # your code here

    for sum in range(0, n+1):
    # 0, 1, 2
        total_f1 = f1(sum)
        total_f2 = f2(sum)
        max_value = max(total_f1, total_f2)
    return max_value

print(max_of_both(2, lambda x:x-1, lambda x:x+1))  # prints 3
print(max_of_both(10, lambda x:x*2, lambda x:x/2))  # prints 20
print("#######################################")

def sublist_sum(L):
    """ L is a list whose elements are lists with int elements
    Returns the sum of all int elements. """
    # your code here
    total_sum = 0
    tot = 0
    for total in L:
        total_sum += sum(total)
        for x in total:
            tot += x

    return (total_sum, tot)

print(sublist_sum([[1,2], [4,5,6]])) # prints 18


#############################################
################## ANSWERS TO AT HOME ####################
#############################################

def max_of_both(n, f1, f2):
    """ n is an int
        f1 and f2 are functions that take in an int and return a float
    Applies f1 and f2 on all numbers between 0 and n (inclusive). 
    Returns the maximum value of all these results.
    """
    # your code here
    maxval = f1(0)
    for i in range(n+1):
        if f1(i) > maxval:
            maxval = f1(i)
        if f2(i) > maxval:
            maxval = f2(i)
    return maxval

# print(max_of_both(2, lambda x:x-1, lambda x:x+1))  # prints 3
# print(max_of_both(10, lambda x:x*2, lambda x:x/2))  # prints 20


def sublist_sum(L):
    """ L is a list whose elements are lists with int elements
    Returns the sum of all int elements. """
    ## One way by using the sum function over the sublist
    tot = 0
    for subL in L:
        tot += sum(subL)
    return tot
    ## Alternate way by nesting a for loop that 
    ## iterates over the sublist's int elements
    tot = 0
    for subL in L:
        for e in subL:
            tot += e
    return tot
    

# print(sublist_sum([[1,2], [4,5,6]])) # prints 18

print(f"######################################################################")
t1 = (1, 'two', 3)
t2 = (t1, 3.25)
print(f"This is t2 {t2}")
print(f"This is t1 + t2 {(t1 + t2)}")
print(f"this is t1 + t2 index  {(t1 + t2)[4]}")
print(f"This is t1 + t2 index  {(t1 + t1)[2:5]}")


def intersect(t1, t2):
    """Assumes t1 and t2 are tuples
    Returns a tuple containing elemnts that are in both t1 and t2"""
    result = ()

    for e in t1:
    # e is 1, "a", 2
        if e in t2:
            result += (e,)
    return result

print(intersect((1, "a", 2), ("b", 2, "a")))


def find_extreme_divisors(n1 , n2):
    """Assumes that n1 and n2 are positive ints
    Return a tuple containing the smallest common divisor > 1 and 
    the largest common divisofr of n1 & n2. If no common diviros,
    other than 1, reutnrs (none, None)"""
    min_val, max_val = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            if min_val == None:
                min_val = i
            max_val = i
    return min_val, max_val

print(find_extreme_divisors(100, 200))

for elem in (1,"a", 2, (3,4)):
    print(elem)

def sum_of_tuples(tup):
    """Write an expression that evaluates to the mean of a tuple of numbmers.
    Use the function sum"""
    # calculate the tuples 
    # sum the content of the tuples
    # average the tuples using the mean function
    total = 0
    for i in tup:
        total += i

    mean_of_tuple = total/len(tup)
    return mean_of_tuple

print(sum_of_tuples((1,3,4,5)))

L = ["Asep draksistema", 5, "gagagugu"]
for i in  L:
    print (i)
print(L[::-1])

print(f"###########################")
L1 = [1,2,3]
L2 = L1[-1::-1]
print(L1)
print(L2)
for i in range(len(L1)):
    # will iterate 3 times
    # 0 , 1 , 2
    print(L1[i]*L2[i])
    # 1 * 3 , 2 * 2, 3 * 1
    # match the index 
    

Techs = ["MIT", "Caltech"]
Ivys = ["Harvard", "Yale", "Brown"]
Techs.append("RPI")

# Combines the two list together
Univs = [Techs, Ivys]
# This one is different ?
Univs1 = [["MIT", "Caltech"], ["Harvard", "Yale", "Brown"]]

print(Univs)
print(Univs1)
print(Univs == Univs1)
print(id(Univs) == id(Univs1)) # test object equality
print(Univs is Univs1)

print(f"################################ ID OF Objects ########################################")
print(f"Id of univs = {id(Univs)}")
print(f"Id of univs1 = {id(Univs1)}")
print(f"Ids of Univs[0] and Univs[1] {id(Univs[0])} {id(Univs[1])}")
print(f"Ids of Univs1[0] and Univs1[1] {id(Univs1[0])} {id(Univs1[1])}")
print(f"##########################################")

L = [1, 2, 3]
L.append(L)
print(L is L[-1])
print(f"############################################")
def append_val(val, list_1 = []):
    list_1.append(val)
    print(list_1)
append_val(3)
list_2 = []
append_val(4, list_2)
print(f"##############################")

Techs.append(Ivys)
print(Techs)

L1 = [1, 2, 3]
L2 = [4, 5 ,6]
L3 = L1 + L2
print(f"L3 = {L3}")
L1.extend(L2)
print(f"L1 = {L1}")
L1.append(L2)
print(f"L1 = {L1}")
print(f"#######################")
L1 = [1, 2, 3]
index_L1 = L1.index(1)
reverse = L1.reverse()
print(index_L1)
print(L1.sort())
print(reverse)
L1.pop(0)
print(L1)



