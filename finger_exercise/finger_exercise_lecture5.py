# Assume you are given a string variable named my_str.
# Write a piece of Python code that prints out a new string containing the even indexed characters of my_str.
# For example, if my_str = "abcdefg" then your code should print out aceg.

my_string = "abcde"
even_chars = ""
lengthofstring = len(my_string)
for i in range(0,lengthofstring,2):
    even_chars += my_string[i]

print(even_chars)
