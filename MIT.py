# ###########################
# #### EXAMPLE: applying functions to repeat same task many times
# ###########################
# #A very simple example of a function that has one
# #argument and returns one value
# def is_even(i):   
#     """Assumes: i, a positive int
#     Returns True if i is even, otherwise False"""
#     if i%2 == 0:
#         return True
#     else:
#         return False

# is_even(3) # <- returns False
# is_even(8) # <- returns True

# print(is_even(3)) # <- prints False
# print(is_even(8)) # <- prints True



# ############## YOU TRY IT ###################
# # Write code that satisfies the following specification:
# def div_by(n, d):
#     """ n and d are ints > 0
#         Returns True if d divides n evenly and False otherwise 
#     """
#     # your code here
#     print(f"inside is_even")
#     if n % d == 0:
#         return True
#     else:
#         return False

# # For example: 
# print(f" 10 divided by 3 is {div_by(10,3)}")     # print False
# print(f" 192 divided by 3 is {div_by(195,13)}")   # returns True

# ##############################################

# # # Using the is_even function later on in the code
# # print("Numbers between 1 and 10: even or odd")

# for i in range(1,100):
#     if is_even(i):
#         print(i, "even")
#     else:
#         print(i, "odd")



# ###########################
# ### EXAMPLE: sum of all odd numbers between (including) a and b
# ###########################
# ## with a for loop
# def sum_odd(a, b):
#     sum_of_odds = 0
#     for i in range(a, b+1):
#         if i%2 == 0:
#             sum_of_odds += i
#             print(i, sum_of_odds)
#     return sum_of_odds

# # print(sum_odd(2,4)) 
# # print(sum_odd(2,7)) 

# # # with a while loop
# def sum_odd(a, b):
#     sum_of_odds = 0
#     i = a
#     while i <= b:
#         if i%2 == 1:
#             sum_of_odds += i
#         i += 1
#     return sum_of_odds

# # print(sum_odd(2,4)) 
# # print(sum_odd(2,7)) 


# ############## YOU TRY IT ###################
# # Write code that satisfies the following specification:
# # Hint, use paper and pen for a strategy before coding!
# def is_palindrome(s):
#     """ s is a string
#     Returns True if s is a palindrome and False otherwise
#     """
#     # your code here
#     s = s.lower()
#     # remove spaces and non-alphanumberic character
#     s = ''.join(char for char in s if char.isalnum())
#     reverse = s[::-1]
#     if s == reverse: ## check whether its palindrome or not
#         print(f"{s[::-1]}")
#         return True
#     else:
#         return False

# print(f"{is_palindrome("racecar")}")
# ################################################

# ################################################
# ################ YOU TRY IT AT HOME #####################
# ################################################
# # 1. Write code that satisfies the following specs:
# def keep_consonants(word):
#     """ word is a string of lowercase letters
#         Returns a string containing only the consonants 
#         of word in the order they appear
#     """
#     # your code here
#     consonants = "bcdefghjklmnpqrstvwxz"
#     consonants_word = ""

#     # iterate throught the word list
#     for char in word:
#         if char in consonants:
#             consonants_word += char
#     return consonants_word


# # For example
# print(keep_consonants("abcd"))  # prints bcd
# print(keep_consonants("aaa"))  # prints an empty string
# print(keep_consonants("babas"))  # prints bbs



# # 2. Write code that satisfies the following specs:
# def first_to_last_diff(s, c):
#     """ s is a string, c is single character string
#         Returns the difference between the index where c first
#         occurs and the index where c last occurs. If c does not 
#         occur in s, returns -1. 
#     """
#     # your code here
#     first_index = -1
#     last_index = -1


#     for i in range(len(s)):
#         if s[i] ==  c:
#             if first_index == -1:
#                 first_index = i
#             last_index = i
#     if first_index == -1:
#         return -1
#     return last_index - first_index

# # For example
# print(first_to_last_diff('aaaa', 'a'))  # prints 3
# print(first_to_last_diff('abcabcabc', 'b'))  # prints 6
# print(first_to_last_diff('abcabcabc', 'd'))  # prints -1


# ################################################
# ################################################
# ################################################

# ################################################
# ########## ANSWERS TO YOU TRY IT #######
# ################################################
# # def div_by(n, d):
# #     """ n and d are ints > 0
# #         Returns True if d divides n evenly and False otherwise 
# #     """
# #     # your code here
# #     # one way
# #     if n%d==0:
# #         return True
# #     else:
# #         return False
# #     # another way: 
# #     # return n%d==0
    
# # print(div_by(10,3))    
# # print(div_by(195,13))    


# # def is_palindrome(s):
# #     """ s is a string
# #     Returns True if s is a palindrome and False otherwise
# #     """
# #     # your code here
# #     for i in range(len(s)//2):
# #         if s[i] != s[len(s)-i-1]:
# #             return False
# #     return True        

# # s="2222"
# # print(is_palindrome(s))

# # s="222"
# # print(is_palindrome(s))

# # s="abc"
# # print(is_palindrome(s))


# ################################################
# ########## ANSWERS TO YOU TRY IT AT HOME #######
# ################################################
# def keep_consonants(word):
#     """ word is a string of lowercase letters
#         Returns a string containing only the consonants 
#         of word in the order they appear
#     """
#     vowels = "aeiou"
#     ans = ""
#     for char in word:
#         if char not in vowels:
#             ans += char
#     return ans

# # For example:
# # print(keep_consonants("abcd"))  # prints bcd
# # print(keep_consonants("aaa"))  # prints an empty string
# # print(keep_consonants("babas"))  # prints bbs


# def first_to_last_diff(s, c):
#     """ s is a string, c is single character string
#         Returns the difference between the index where c first
#         occurs and the index where c last occurs. If c does not 
#         occur in s, returns -1. 
#     """
#     if c not in s:
#         return -1
#     # if reach here, c is in s
#     for i in range(len(s)):
#         if s[i]==c:
#             # break here to save i as the first instance of c in s
#             break
#     # loop through s backwards
#     for j in range(len(s)-1,-1,-1):
#         if s[j]==c:
#             # break here to save j as the last instance of c in s
#             break
#     # this return is ok becasue the loops iterated through indices not chars of s
#     return j-i

# For example
# print(first_to_last_diff('aaaa', 'a'))  # prints 3
# print(first_to_last_diff('abcabcabc', 'b'))  # prints 6
# print(first_to_last_diff('xyz', 'b'))  # prints -1

################################################
################################################
################################################

def find_root(x, power, epsilon):
    #Find interval containing answer
    if x < 0 and power%2 == 0:
        return None #Negative number has no even-powered roots
    low = min(-1,x)
    high = max(1,x)

    # Use bisection search

    ans = (high + low)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else: 
            high = ans
        ans = (high + low) / 2
    return ans
print(find_root(25, 2, 0.0001))
print(find_root(-8, 3, 0.0001))
# print(find_root(16, 4, 0.0001))

# def is_in(a, c):
#     for i in range(len(a)):
#         if a[i] in c:
#             return True
    
    
    
#     return False
        
    
# print(is_in("abc","bcd"))

# def test_is_in(a, c):
#     for first_string in a:
#         for second_string in c:
#             result = is_in(first_string, second_string)
#             if result:
#                 value = "Okay"
#             else:
#                 value = "There is no onccurence of the same letter in both strings"

#             print(f"first string: {first_string}, second:{second_string} : {value}")

# first_string = ("gugugaga", "gagagugu")
# second_string = ("abababaa", "guramegigigugu")
# test_is_in(first_string,second_string)


# def print_name(first_name, second_name, reverse = False):
#     if reverse:
#         print(f"{second_name} {first_name}")
#     else:
#         print(f"{first_name} {second_name}")

# print_name("Boris", "Vorontsov", False)

# print_name("Boris", "Vorontsov", True)

# print_name(second_name = 'Puchmajerova', first_name = 'Olga')

# def multiplier(*args):
#     if len(args) == 1:
#         print(args[0])
#     elif len(args) == 2:
#         print(args[0] * args[1])
#     else:
#         print(f"Too much arguments can't take it!")

# result = multiplier(5,10)
# print(f"{result}")


# def f(x):
#     y = 1
#     x = x + y
#     print(f"x = {x}")
#     return x
# x = 3
# y = 2
# z = f(x) #value of x used as ac tual parameter
# print(f"z = {z}")
# print(f"x = {x}")
# print(f"y = {y}")


def f(x):
    def g():
        x = "abc"
        print(f" x = {x}")

    def h():
        z = x
        print(f"z = {z}")

    x = x + 1
    print(f"x = {x}")

    h()
    g()
    
    print(f"x = {x}")

    return g

x = 3
z = f(x)
print(f" x = {x}")
print(f"z = {z}")
z()


def log(x, base, epsilon):
# Find lower bound on ans

    lower_bound = 0
    while base**lower_bound < x:
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1
# Perfrom bisection search

    ans = (high + low) / 2
    while abs(base**ans - x) >= epsilon:
        if 2**ans < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/ 2
    return ans


print(log(100, 10, 0.01))










