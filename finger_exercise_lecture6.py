# Assume you are given an integer 0 \<= N \\<= 1000. Write a piece of Python code that uses bisection search to guess N.
# The code prints two lines: count: with how many guesses it took to find N, and answer: with the value of N.
# Hints: If the halfway value is exactly in between two integers, choose the smaller one.

N = 35

# epsilon = 0.0001
# num_guesses = 0
# high = 1000
# low = 0.0
# guess = (high + low) / 2
# 
# while abs(guess - N) >= epsilon:
#     # find the N value
#     if guess < N:
#         low = guess
#     else:
#         high = guess
#     print(f"{low} and {high}")
#     guess = (high + low) / 2
#     num_guesses += 1
# print(f"num_guesses = {str(num_guesses)}")
# print(f"the number is {guess}")

low = 0
high = 1001
guess = (high+low)//2
count = 1
while guess != N:
    if guess < N:
        low = guess + 1
    elif guess > N:
        high = guess - 1
    guess = (high+low)//2
    count += 1
print("count:",count)
print("answer:",guess)