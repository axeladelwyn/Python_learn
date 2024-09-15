import time

## -------------------------------------------------- ##
## EXAMPLE: timing a program
## -------------------------------------------------- ##

# constant fcn
def c_to_f(c):
    return c*9.0/5 + 32
# linear fcn -- finds 0+1+2+...+x
def mysum(x):
    total = 0
    for i in range(x+1):
        total += i
    return total

# quadratic fcn -- finds n*n inefficiently
def square(n):
    sqsum = 0
    for i in range(n):
        for j in range(n):
            sqsum += 1
    return sqsum

# helper function to show timing
def time_wrapper(f, L):
    print('Timing', f.__name__)
    for i in L:
        t = time.time()
        f(i)
        dt = time.time()-t
        print (f"{f.__name__}({i}) took {dt} sec")

##creates a list [1, 10, 100, ...] to test different input sizes
L_N = [1]
for i in range(8):
    L_N.append(L_N[-1]*10)
print(L_N)
## time each function
# time_wrapper(c_to_f,  L_N)
# time_wrapper(mysum, L_N)
# time_wrapper(square, L_N)  # caution this will take 500 sec, then 50000 sec


## -------------------------------------------------- ##
## EXAMPLE: counting the number of operations
## -------------------------------------------------- ##

## constant fcn with counting the number of ops
def c_to_f(c):
    counter = 3
    return (counter, c*9.0/5 + 32)

# linear fcn  with counting the number of ops
def mysum(x):
    counter = 1
    total = 0
    for i in range(x+1):
        counter += 3
        total += i
    return (counter, total)

# quadratic fcn  with counting the number of ops
def square(n):
    counter = 1
    mysum = 0
    for i in range(n):
        counter += 1
        for j in range(n):
            counter += 3
            mysum += 1
    return (counter, mysum)

# helper function to show number of operations
def count_wrapper(f, L):
    print('Counting', f.__name__)
    for i in L:
        counter = f(i)[0]
        if i == min(L):
            multiplier = 1.0
        else:
            multiplier = counter/float(prev)
        prev = counter
        print(f"{f.__name__}({i}): {counter} ops, {round(multiplier,5)} x more")


L1 = [100]
for i in range(5):
    L1.append(L1[-1]*10)

L2_a = [128, 256, 512, 1024, 2048, 4096, 8192]
L2_b = [1, 10, 100, 1000, 10000]
# count_wrapper(c_to_f, L1)
# count_wrapper(mysum, L1)
# count_wrapper(square, L2_a)
# count_wrapper(square, L2_b)
def g(L, e):
    for i in range(100):
        for e1 in L:
            if e1 == e:
                return True
    return False
# O(n)
def h (L, e):
    for i in range(e):
        for e1 in L:
            if e1 == e:
                return True
    return False
# O(e * n)

def int_to_str(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i//10
    return result
convert = int_to_str(500)
print(convert)

# fib_cache = {}

# def fibonnaci(n):
#     if n in fib_cache:
#         return fib_cache[n]
    
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1

#     fib_cache[n] = fibonnaci(n-1) + fibonnaci(n-2)

#     return fib_cache[n]

# print(fibonnaci(15))
# print(fib_cache)
# print(fib_cache[2])

def f(x):
    ans = 0
    # constant time
    for i in range(1000):
        ans += 1
    print("Number of additions so far" , ans)
    # takes time x
    for i in range(x):
        ans += 1
    print("Number of additions so far" , ans)
    for i in range(x):
        for j in range(x):
            ans += 1
            ans += 1
    print("Number of additions so far" , ans)
    return ans
answer = f(1000)
print(answer)    


def add_digits(n):
    string_rep = int_to_str(n)
    val = 0
    for c in string_rep:
        val += int(c)
    return val
digits = add_digits(500)
print(digits)


def is_subset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
L1 = [1,2,3]
L2 = [2,3,4]
print(is_subset(L1,L2))


def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
                break
    result = []
    for e in tmp:
        if e not in result:
            result.append(e)
    return result
print(intersect(L1, L2))