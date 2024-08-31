import math
# Problem 1 - Bisection Search Practise
# Write a program using bisection search to find the forth root of a number inputted by the 
# user. Print the forth root calculated with max error of 0.01. 

# x = float(input("Using bisection search calculate the forth root of: " ))
# epsilon = 0.01
# low = 0
# high = x
# ans = (high + low) / 2.0

# while abs(ans**4 - x) >= epsilon:
#     if ans**4 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low) / 2.0
# print(f"the answer is {ans}")



# Problem 2 - Functions 
# Write a Python function to check whether a number falls in a given range. 

def num_check(number):
    number_high = number + 50
    number_low = number - 50
    print (f"{number} is within the range of {number_low} and {number_high}")
    return number
    # check the number
    # return number list
num_check(50)

# Problem 3 - Functions 
# Write a Python function to check whether a number is perfect or not.
# (In number theory, a perfect number is a positive integer that is equal 
# to the sum of its proper positive divisors, excluding the number itself).


def perfect_square(number):

    square_number = math.sqrt(number)
        
    return square_number.is_integer()


print(f"{perfect_square(25)}")
print(f"{perfect_square(37)}")
print(f"{perfect_square(49)}")
number = [24, 25, 25, 37, 39 , 40]

for num in number:
    if perfect_square(num):
        print(f"{num} is a perfect square")
    else:
        print(f"{num} is a not a perfect square")







# Problem 4 - Approximation Algorithm (see Lecture 5 slides for similar problem)
# Write an approximation algorithm to calculate the forth root of some 
# number inputted by the user. 
# Print the result and the number of iterations required to reach that result. 
# The program should not accept negative numbers. Initial parameters epsilon 
# (i.e. accuracy), initial guess, increment and num_guesses are defined below.

# example initial parameters
# x = int(input(f"Please input a number that will be calculated to find the fourth root "))
# epsilon = 0.01
# ans = 0.0
# increment = epsilon**2
# num_guesses = 0

# while abs(ans**4 - x) >= epsilon and ans <= x:
#     num_guesses +=1
#     ans += increment
# print(f"number of guesses = {num_guesses}")
# if abs(ans**4 - x) >= epsilon:
#     print(f"Failed on square root of {x}")
# else:
#     print(f"{ans} is approximation fourth root of {x}")



