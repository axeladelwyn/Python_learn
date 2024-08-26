####################################################################################
# Practice Problem 1
# Write a program that takes your name as an Input and Outputs the length of your name minus 5.

# Insert code below

#insert_name = input("Put your name: ")
#name_length = len(insert_name) - 5
#print(str(name_length))

####################################################################################
# Practice Problem 2
# Write a program to remove the nth character from a non empty string.
# Print the old string and the new string.

# test_string = "We want to remove the nth character from this string"
# n = 8
# 
# # Insert code below
# nth_character = int(input(f"Enter which nth character you want to remove "))
# print(f"Old string is : {test_string}")
# modified_string = test_string[:nth_character] + test_string[nth_character + 1:]
# print(f"{modified_string}")
# 
# 
####################################################################################
# Practice Problem 3
# Write a program which answers the following:
# Does a given string have length greater than 10 or less than 5? If True, output True. If False, output False.

my_string = "This is my string"  # example string - modify to test

# Insert code below
string_length = len(my_string)

if string_length > 10:
    print(True)
else:
    print(False)


####################################################################################
# Practice Problem 4
# Write a program which answers the following using a for loop:
# Count the number of e's in the following string

my_string = "How many times is the letter e in this string?"

# Insert code below
count = 0
char_to_count = 'e'
for char in my_string:
    if char == char_to_count:
        count += 1
print(count)






