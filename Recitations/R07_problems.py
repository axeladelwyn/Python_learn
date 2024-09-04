# Dictionaries Practice

# Problem 1: 
# Write a function that takes as input a dictionary and returns a new dictionary,
# where 5 is added to each value of the original dictionary, assuming all values are integers.
# e.g
# {"item1": 2, "item2": 7, "item3": 20} returns {"item1": 7, "item2": 12, "item3": 25}
def new_dict(input_dict):
    for k, v in input_dict.items():
        input_dict[k] = v + 5
    return input_dict
    
input_dict = {"item1": 2, "item2": 7, "item3": 20}
print(new_dict({"item1": 2, "item2": 7, "item3": 20})) # expect {"item1": 7, "item2": 12, "item3": 25}


print(f"###############PROBLEM2####################")
# Problem 2:
# Write a function to check all values are same in a dictionary. 
# Return True if they are all the same, False otherwise
# e.g 
# {'item1': 'apple', 'item2': 'apple', 'item3': 'apple'} returns True, 
# {'item1': 'apple', 'item2': 'apple', 'item3': 'orange'} return False

def check_same_values(input_dict):
    # return a boolean
    values = list(input_dict.values())
    print(values)
    first_values = values[0]
    for value in values:
        if value != first_values:
            return False
    return True

# testing
input_dict = {'item1': 'apple', 'item2': 'apple', 'item3': 'apple'}
print(check_same_values(input_dict))  # expect True
input_dict = {'item1': 'apple', 'item2': 'apple', 'item3': 'orange'}
print(check_same_values(input_dict))  # expect False

print(f"#################PROBLEM 3######################")

# Problem 3: 
# Convert a dictionary to a list of lists where each sublist is in the 
# form [key, value]. Return a sorted version of this list where we sort 
# by decreasing values. 
# Example input: {'a': 1, 'b': 5, 'c': 10, 'd': 3, 'e': 2} 
# Example output: [['c', 10], ['b', 5], ['d', 3], ['e', 2], ['a', 1]]

def dict_to_sorted_list(input_dict):
    
    combined_list = [[k,v] for k, v in input_dict.items()]
    sorted_list = sorted(combined_list, key=lambda x: x[0])
    return sorted_list

# testing
input_dict = {'a': 1, 'b': 5, 'c': 10, 'd': 3, 'e': 2}  
print(dict_to_sorted_list(input_dict))  # expect: [['c', 10], ['b', 5], ['d', 3], ['e', 2], ['a', 1]]


print("##############PROBLEM 4##############")
# Problem 4:
# Given a list of dictionaries with item names and amounts in the form {'item': 'my_item_name', 'amount': 'my_amount'}
# write function to combine these items into a single dictionary. See example below. 
# Example input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: {'item1': 1150, 'item2': 300}

def combine_dicts(input_dicts):
    # combine into single dictionary
    my_dict = {}
    for element in input_dicts:
        item = element['item'] #assign 'item' key to a variable
        amount = element['amount'] # assign the value of 'amount' to a variable amount
        print(item)
        print(amount)
        if item in my_dict:
            my_dict[item] += amount
        else:
            my_dict[item] = amount
    return my_dict

# testing
input_dicts = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
print(combine_dicts(input_dicts))  # expect {'item1': 1150, 'item2': 300}
print(f"###############################################")
capitals = {"Japan": "Tokyo", "France": "Paris", "German": "Berlin"}
for key in capitals:
    print(f"The Capital of {key} is {capitals[key]}")

cities = []
for value in capitals.values():
    cities.append(value)
print(f"{cities}, is a list of capital cities in the world")
capital_value = capitals.values()
print(capital_value)
print(f"#####################CLASS#####################")
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return (f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        return (f"{self.name} says Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())


def get_min(d):
    """d is a dict mapping letter to ints 
    retursn the value in d with the key that occursd first in the alphabet.
    E.g., if d = {x = 11, b = 12 }, get_min returns 12."""
    alphabet = "abcdefgijklmnopqrstuvwxyz"
    # my_dict = {}
    # for k,v in sorted(d.items()):
    #     my_dict[k] = v
    # print(my_dict)
    
    # for k,v in my_dict.items():
    #     if k in alphabet:
    #         return v
    #     else:
    #         raise ValueError("{k} is not in the alphabet")
    min_key = min(d.keys(), key=lambda k: alphabet.index(k))

    print(f"The value of min_key is {min_key}")
    return d[min_key]


dictionary = {"x": 11, "b": 12} 
print(get_min(dictionary))