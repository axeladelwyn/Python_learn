import random

#################################
## Animal abstract data type 
#################################
class Animal(object):
    def __init__(self, age): # The parameters stays 1 but the attribute can be added? # can be just set __init__ with a infinite amount of parameter 
        # to make the code more simplers?
        self.age = age
        self.name = None
        self.color = None
        # you can set basically infinite attribute to a class 
        # such as type, genes, order, genus , classification etc..
    def __str__(self):
        return "animal name:"+str(self.name)+" age: "+str(self.age)+" Color: "+str(self.color)
    def get_age(self):           ################
        return self.age          ##############
    def get_name(self):         ############## GETTERS
        return self.name        ################
    def get_color(self):
        return self.color
    def set_age(self, newage): ######################
        self.age = newage       #####################
    def set_name(self, newname=""): ############## SETTERS
        self.name = newname         ################
    def set_skin_color(self, color= ""):
        self.color = color
b = Animal(5)
new_name = b.set_name("baristook")
new_age = b.set_age(30)
c = b.get_name()
d = b.get_age()
print(b)
print(c)
print(d)

my_dog = Animal(10)
my_dog.set_name("Doggy")
my_dog.set_age(25)
my_dog.set_skin_color("blue yellowish red")
dog_age = my_dog.get_age()
print(my_dog)
print(dog_age)
# #default parameters with methods        
a = Animal(4)
# print(a)
b = Animal(6)
# print(b)
# print(a.age)
# print(a.get_age())

# a.set_name("fluffy")
# print(a.name)
# print(a.get_name())
# print(a)
# a.set_name()
# print(a)

# #Accessing data attributes and adding new attributes (just for one instance)
# #These are bad to do, use getter and setter methods instead!
# a = Animal(4)
# a.name = "furball"
# a.age = "twelve"
# a.size = "tiny"
# print(a.get_age())

print(f"########################")
### EXAMPLE: using Animal objects in code
def animal_dict(L):
    """ L is a list
    Returns a dict, d, mappping an int to an Animal object. 
    A key in d is all non-negative ints, n, in L. A value 
    corresponding to a key is an Animal object with n as its age. """
    d = {}
    for n in L:
        # if type of an L iteration which is n is integer and n is greater or equal to 0
        # which means it cannot be negative in order to pass
        # set the dictionary to a animal class?
        if type(n) == int and n >= 0:
            # what does this line do?
            d[n] = Animal(n) #change this ? This is assignin key value pair in dictionary d {}
    return d # this return a dictionary

L = [2,5,'a',-5,0]
animals = animal_dict(L) # or this?
dog_animals = animal_dict(L)
print(dog_animals) # why it prints the memory location?
# 3 number get picked from L which is 2, 5, 0 
# how do i display the animal age
for key, value in dog_animals.items():
    print(f"Age: {key} , Animal class: {value}")

# print(animals)
# above prints {2: <__main__.Animal object at 0x00000199AFF350A0>, this is a dictionary
#               5: <__main__.Animal object at 0x00000199AFF35A30>, this is a dictionary
#               0: <__main__.Animal object at 0x00000199AFF35D00>} this is a dictionary

for n,a in animals.items():   
    print(f'key {n} with val {a}')
# loop above prints animal:None:2 
#                   animal:None:5 
#                   animal:None:0
print(f"################")
###################### YOU TRY IT ####################
# Write a function that smeets this spec.
def make_animals(L1, L2, L3):
    """ L1 is a list if ints and L2 is a list of str
        L1 and L2 have the same length
    Creates a list of Animals the same length as L1 and L2.
    An animal object at index i has the age and name
    corresponding to the same index in L1 and L2, respectively. """
    # your code here
    #L1 is list of ints
    #L2 is list of string
    # put it together
    # create a list of animals 
    # index i is age and name
    # L1 for age and L2 for name(string)
    combind_list = [] # this is the combined list
    for i in range(len(L1)):
        age = L1[i]
        name = L2[i]
        color = L3[i]
        a = Animal(age)
        a.set_name(name)
        a.set_skin_color(color)
        combind_list.append(a)
        # put a square bracket inside it``
        # append iteration and string of L2
        # add a list in list pair such as [[2,blobflish],[5,crazyant],...]
        # how to do that??
        # It added three element
    return combind_list
L1 = [2,5,1]
L2 = ["blobfish", "crazyant", "parafox"]
L3 = ["red", "blue", "green"]
animals = make_animals(L1, L2, L3)
print(animals)
for i in animals:
    print(i)
# animals = make_animals(L1, L2)
# print(animals)     # note this prints a list of animal objects
# for i in animals:  # this prints the indivdual animals
#     print(i)

#######################################################


#################################
# connected to Animal class that's written above
## Inheritance example 
#################################
class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)+":"+str(self.color) # override previous class __str__
    # cat go to interdimensional rift and bring back futuristic techonology 

    
#print("\n---- cat tests ----")
my_cat = Cat(5)
my_cat.speak() # you don't need to print it
my_cat.set_name("baritooks")
my_cat.set_skin_color("white")
print(my_cat.get_age())
print(my_cat)
c = Cat(5)
c.set_name("fluffy")
print(c)
c.speak()
print(c.get_age())
# a.speak() # error because there is no speak method for Animal class
print(f"#############################")

################# YOU TRY IT #####################
class Rabbit(Animal):
    """ A subclass of Animal """
    def speak(self):
        """ prints the string meep to the console """
        # your code here
        print("Meeps!")

    def __str__(self):
        """ Repr as "rabbit", a colon, self's name, a colon, self's age """
        # your code here
        return (f"Animal is: {self.name}, age is: {self.age}, and the color is {self.color}")
   
r = Rabbit(5)
print(r)
r.speak()
r.set_name('fluffy')
print(r)

my_rabbit = Rabbit(7)
print(my_rabbit.get_age())
print(my_rabbit.get_name())
my_rabbit.set_name("Bubble")
print(my_rabbit.get_name())
my_rabbit.set_skin_color("blue")
print(my_rabbit.get_color()) # get the color from the function
##################################
print(f"### Inheritance example")
##################################
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
    def get_friends(self):
        return self.friends.copy()
    def speak(self):
        print("hello")
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)

#print("\n---- person tests ----")

person1 = Person("Asep", 25)
print(person1)
person1.add_friend('Ujang') # List all the friends in a list
print(person1.get_friends())
person1.speak() #print "hello"
person2 = Person("RahmatBungkakaresh", 30)
person1.age_diff(person2) # There is 5 years difference betewen asep and rahmhat
print(person1.get_age())
p1 = Person("jack", 30)
p2 = Person("jill", 25)
# print(p1.get_name())
# print(p1.get_age())
# print(p2.get_name())
# print(p2.get_age())
# print(p1)
# p1.speak()
# p1.age_diff(p2)
# p1.add_friend('ana')
# p1.add_friend('bob')
# p1.add_friend('bob')
# print(p1.get_friends())
print(f"################")
######################## YOU TRY IT #####################
# Write the function according to this spec
def make_pets(d):
    """ d is a dict mapping a Person obj to a Cat obj
    Prints, on each line, the name of a person, 
    a colon, and the name of that person's cat """
    # your code here
    # map a person name and a person cat 
    # Person(Animal) and Cat(Animal)
    for k,v in d.items():
        # k is person
        # v is cat
        # get_name() from the class attributes
        print(k.get_name()+":"+v.get_name()) # we need to print it because its returns something
p1 = Person("ana", 86)
p2 = Person("james", 7)
c1 = Cat(1)
c1.set_name("furball")
c2 = Cat(1)
c2.set_name("fluffsphere")

d = {p1:c1, p2:c2}
make_pets(d)  # prints ana:furball
       #        james:fluffsphere

##########################################################
print(f"##################################")
##################################
### Inheritance example
##################################
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("--> i have homework")
        elif 0.25 <= r < 0.5:
            print("--> i need sleep")
        elif 0.5 <= r < 0.75:
            print("--> i should eat")
        else:
            print("--> i'm zooming")

student1 = Student("boris", 25, "Computer science")
student1.add_friend("Jacobian A")
print(student1.get_friends()) # so basically get friends from the class person still works on this class
student1.set_skin_color("blue")
print(student1.get_color()) # added a blue attribute on skin color

student1.speak() #prints the random proabilities on speak function withint student class
# print("\n---- student tests ----")
s1 = Student('alice', 20, "CS")
s2 = Student('beth', 18)
# print(s1)
# print(s2)
# print(s1.get_name(),"says:")
# s1.speak()
# print(s2.get_name(),"says:")
# s2.speak()


##################################
print(f"### Use of class variables########" )
##################################
class Rabbit(Animal):
    # rabbit Class that inherit an animal class
    # a class variable, tag, shared across all instances
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.p1 = parent1
        self.p2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):
        # zfill used to add leading zeroes 
        # 00001 instead of 1 or 00526 instead of 526
        return str(self.rid).zfill(5)
    def get_parent1(self):
        return self.p1
    def get_parent2(self):
        return self.p2
    def __add__(self, oth):
        # returning object of same type as this class
        return Rabbit(0, self, oth)
        # adding rabbit together?
    def __eq__(self, oth):
        # compare the ids of self and other's parents
        # don't care about the order of the parents
        parents_same = (self.p1.rid == oth.p1.rid and self.p2.rid == oth.p2.rid)
        parents_opp = (self.p2.rid == oth.p1.rid and self.p1.rid == oth.p2.rid)
        return parents_same or parents_opp
    def __str__(self):
        return "rabbit:"+ self.get_rid()

# # print("\n---- rabbit tests ----")
# # print("---- testing creating rabbits ----")
r1 = Rabbit(3)
print(r1.get_age()) # the age of rabbit1 is 3 years old
print(r1.get_parent1()) # rabbit1 doesn't have a parents
print(r1.get_parent2())

r2 = Rabbit(4)
r3 = Rabbit(5)
rabbit_combination = r1 + r2
print(rabbit_combination)
print("r1:", r1)
print("r2:", r2)
print("r3:", r3)
print("r1 parent1:", r1.get_parent1())
print("r1 parent2:", r1.get_parent2())

print("---- testing rabbit addition ----")
r4 = r1+r2   # r1.__add__(r2)
print("r1:", r1)
print("r2:", r2)
print("r4:", r4)
print("r4 parent1:", r4.get_parent1()) # the parents of rabbit4 is rabbit 1 and rabbit 2
print("r4 parent2:", r4.get_parent2()) 

# # print("---- testing rabbit equality ----")
r5 = r3+r4
r6 = r4+r3
r7 = r3+r4
r7.set_skin_color("green")
print(r7.get_color()) # added  color to rabbit 7 
print(r6==r7) #this returns True because the parents is  the same which is rabbit 4 and rabbit 3
# print("r3:", r3)
# print("r4:", r4)
# print("r5:", r5)
# print("r6:", r6)
# print("r5 parent1:", r5.get_parent1())
# print("r5 parent2:", r5.get_parent2())
# print("r6 parent1:", r6.get_parent1())
# print("r6 parent2:", r6.get_parent2())
# print("r5 and r6 have same parents?", r5 == r6)
# print("r4 and r6 have same parents?", r4 == r6)


##################################################
######### ANSWERS TO YOU TRY IT ###############
##################################################

# Q1. Write a function that meets this spec.
def make_animals(L1, L2):
    """ L1 is a list if ints and L2 is a list of str
        L1 and L2 have the same length
    Creates a list of Animals the same length as L1 and L2.
    An animal object at index i has the age and name
    corresponding to the same index in L1 and L2, respectively. """
    pass
    L = []
    for i in range(len(L1)):  # i will be 0 then 1 then 2
        a = Animal(L1[i]) # L1[i] is the age
        a.set_name(L2[i]) # L2[i] is the name
        L.append(a)
    return L        

# L1 = [2,5,1]
# L2 = ["blobfish", "crazyant", "parafox"]
# animals = make_animals(L1, L2)
# print(animals)     # note this prints a list of animal objects
# for i in animals:  # this prints the indivdual animals
#     print(i)

# Q2. 
class Rabbit(Animal):
    """ A subclass of Animal """
    def speak(self):
        """ prints the string meep to the console """
        print('meep')
    def __str__(self):
        """ Repr as "rabbit", a colon, its name, a colon, its age """
        return "rabbit:"+str(self.get_name())+":"+str(self.get_age())
   
# c = Rabbit(5)
# print(c)
# c.speak()
# c.set_name('fluffy')
# print(c)


# Q3. Write the function according to this spec
def make_pets(d):
    """ d is a dict mapping a Person obj to a Cat obj
    Prints the name of each person, a colon, and the 
    name of that person's cat """
    pass
    for k,v in d.items():
        # k is Person
        # v is Cat
        pname = k.get_name()
        cname = v.get_name()
        print(pname+":"+cname)


# p1 = Person("ana", 35)
# p2 = Person("james", 6)
# c1 = Cat(1)
# c1.set_name("furball")
# c2 = Cat(1)
# c2.set_name("fluffsphere")

# d = {p1:c1, p2:c2}
# make_pets(d)  # prints ana:furball
#       #        james:fluffsphere


##################################################
print(f"######### AT HOME ###############")
##################################################
# Write the class Employee as a subclass of Person
class Employee(Person):
    """ An Employee contains an extra data attribute, salary as an int """
    def __init__(self, name, age):
        """ initializes self as a Person with a salary data attribute, initially 0 """
        self.name = name
        self.age = age
        self.salary = 0
    def get_salary(self):
        """ returns self's salary """
        return self.salary # the salary which is 0 at beginning
    def set_salary(self, s):
        """ s is an int
        Sets self's salary data attribute to s """
        pass
    def salary_change(self, n):
        """ n is an int (positive or negative)
        Adds n to self's salary. If the result is negative, sets 
        self's salary to 0. Otherwise sets self's salary to the new value. """
        pass
    def has_friends(self):
        """ Returns True if self's friend list is empty and False otherwise """
        pass    
    def past_salaries_list(self):
        """ Keeps track of all salaries self has had in the order they've changed. 
        i.e. whenever the salary changes, keep track of it.
        Hint: you may need to add an additional data attribute to Employee.
        Returns a copy of the list of all salaries self has had, in order. """
        pass
    def past_salary_freq(self):
        """ Returns a dictionary where the key is a salary number and the 
        value is how many times self's salary has changed to that number. """
        pass

# # For example:
# e = Employee("ana", 35)
# print(e.get_salary())   # prints 0
# e.set_salary(1000)
# print(e.get_salary())   # prints 1000
# e.salary_change(2000)
# print(e.get_salary())   # prints 3000
# e.salary_change(-50000)
# print(e.get_salary())   # prints 0
# print(e.has_friends())  # prints False
# e.add_friend("bob")
# print(e.has_friends())  # prints True
# print(e.past_salaries_list())  # prints [0, 1000, 3000, 0]
# print(e.past_salary_freq())  # prints {0: 2, 1000: 1, 3000: 1}


# Write a function that meets this specification
def counts(L):
    """ L is a list of Employee and Person objects 
    Returns a tuple of a count of:
      * how many Person objects are in L
      * how many Employee objects are in L 
      * the number of unique names among Employee and Person objects """
    pass

# For example:
# make employees and people
# L = []
# L.append(Person('ana',8))
# L.append(Person('bob',25))
# L.append(Employee('ana',35))
# L.append(Employee('cara',18))
# L.append(Employee('dan',53))
# # call function
# print(counts(L))    # prints (2,3,4)


##################################################
######### ANSWERS TO AT HOME #######
################################################
class Employee(Person):
    """ An Employee contains an extra data attribute, salary as an int """
    def __init__(self, name, age):
        """ initializes self as a Person with a salary data attribute, initially 0 """
        Person.__init__(self,name, age)
        self.salary = 0
        self.list_salaries = [0]
    def get_salary(self):
        """ returns self's salary """
        return self.salary
    def set_salary(self, s):
        """ s is an int
        Sets self's salary data attribute to s """
        self.salary = s
        self.list_salaries.append(s)
    def salary_change(self, n):
        """ n is an int (positive or negative)
        Adds n to self's salary. If the result is negative, sets 
        self's salary to 0. Otherwise sets self's salary to the new value. """
        a = self.salary + n
        if a < 0:
            self.salary = 0
        else:
            self.salary = a
        self.list_salaries.append(self.salary)
    def has_friends(self):
        """ Returns True if self's friend list is empty and False otherwise """
        return len(self.friends) != 0
    def past_salaries_list(self):
        """ Keeps track of all salaries self has had in the order they've changed. 
        i.e. whenever the salary changes, keep track of it.
        Hint: you may need to add an additional data attribute to Employee.
        Returns a copy of the list of all salaries self has had, in order. """
        return self.list_salaries.copy()
    def past_salary_freq(self):
        """ Keeps track of all salaries self has had in the order they've changed. 
        i.e. whenever the salary changes, keep track of it.
        Hint: you may need to add an additional data attribute to Employee.
        Returns a dictionary where the key is a salary number and the value 
        is how many times self's salary has changed to that value. """
        d = {}
        for i in self.list_salaries:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return d
    
# # For example:
# e = Employee("ana", 35)
# print(e.get_salary())   # prints 0
# e.set_salary(1000)
# print(e.get_salary())   # prints 1000
# e.salary_change(2000)
# print(e.get_salary())   # prints 3000
# e.salary_change(-50000)
# print(e.get_salary())   # prints 0
# print(e.has_friends())  # prints False
# e.add_friend("bob")
# print(e.has_friends())  # prints True
# print(e.past_salaries_list())  # prints [0, 1000, 3000, 0]
# print(e.past_salary_freq())  # prints {0: 2, 1000: 1, 3000: 1}


# def counts(L):
#     """ L is a list of Employee and Person objects 
#     Returns a tuple of a count of:
#       * how many Person objects are in L
#       * how many Employee objects are in L 
#       * the number of unique names among Employee and Person objects """
#     counte, countp, countn = 0,0,0
#     names = []
#     for i in L:
#         if type(i) == Person:
#             countp += 1
#         elif type(i) == Employee:
#             counte += 1
#         if i.get_name() not in names:
#             names.append(i.get_name())
#             countn += 1
#     return (countp, counte, countn)

# For example:
# make employees and people
# L = []
# L.append(Person('ana',8))
# L.append(Person('bob',25))
# L.append(Employee('ana',35))
# L.append(Employee('cara',18))
# L.append(Employee('dan',53))
# # call function
# print(counts(L))    # prints (2,3,4)


x = 0
if x == 0:
    print("x is equal to zero")
elif x >= 0:
    print("x is greater than zero")
else:
    print("x is less than zero")


class Person(object):
    def __init__(self,name):
        """Assumes name a string. Create a person"""
        self._name = name
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank+1:]
        except:
            self._last_name = name
        self.birthday = None

    def get_name(self):
        """Returns self's full name"""
        return self._name

    def get_last_name(self):
        """Return self's last name"""
        return self._last_name

    def set_birthday(self, birthdate):
        """Returns self's last name"""
        return self._last_name
    
    def get_age(self):
        """Returns self's current gae in days"""
        if self._birthday == None:
            raise ValueError
        return (datetime.date.today() - self._birthday).days

    def __lt__(self, other):
        """Assume other a Person Returns True if self precedes other in alphabetical order, and False otherwise.
        Comparison is based on last names, but fi these are the same full name are compared."""
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name
    def __str__(self):
        """Returns self's name"""
        return self._name


class MIT_person(Person):
    _next_id_num = 0 #identification number

    def __init__(self, name):
        super().__init__(name)
        self.id_num = MIT_person._next_id_num
        MIT_person._next_id_num += 1
    def get_id_num(self):
        return self.id_num

    def __lt__(self, other):
        return self.id_num < other.id_num

    def is_student(self):
        return isinstance(self, Student)

p1 = MIT_person("Barbara beaver")
p1 = MIT_person("Martk Guttag")
p2 = MIT_person("Billy Bob Beaver")
p3 = MIT_person("Billy Bob Beaver")
p4 = Person("Bily Bob Beaver")
print(str(p1) + "\'s id number is " + str(p1.get_id_num()))

print("p1 < p2 = ", p1 < p2)
print("p3 < p2 = ", p3 < p2)
print("p4 < p1 = ", p4 < p1)


print(isinstance('ab', str) == isinstance(str, str))

print(f"############################")
class Politician(Person):
    """A politician is a person who can belong to a political party"""
    def __init__(self, name, party = None):
        """ name and party are strings"""
        self._name = name
        self.party = party
    def get_party(self):
        """returns the party to which self belongs"""
        return self.party
    def might_agree(self, other):
        """ returns True if self and other belong to the same party or at
        least one of them does not belong to a party"""
        if self.party == other.party or self.party is None or other.party is None:
            return True
        return False

politician1 = Politician("Alice", "Party A")
politician2 = Politician("Bob", "Party A")
politician3 = Politician("Jacib", "Party B")

print(politician3)

print(politician1.might_agree(politician2)) # this will print tru because both of them in party A

class Student(MIT_person):
    pass

class UG(Student):
    def __init__(self,name, class_year):
        super().__init__(name)
        self._year = class_year
    def get_class(self):
        return self._year

class Grad(Student):
    pass

p5 = Grad("Buzz Aldrin")
p6 = UG("Billy Beaver", 1984)
print(f"{p5} is a graduate student is {isinstance(p5, Grad)}")
print(f"{p5} is a undergraduate student is {isinstance(p5, UG)}")


print(f"{p5} is a student is {p5.is_student()}")
print(f"{p6} is a student is {p6.is_student()}")
print(f"{p3} is a student is {p3.is_student()}")