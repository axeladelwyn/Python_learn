class Container(object):
    """
    A containre object is a list and can store elmements of any type
    """
    def __init__(self):
        """ 
        Initialize an empty list
        """
        self.myList = []
    def size(self):
        """ 
        Returns the length of the container list
        """
        return len(self.myList)
    def add(self,elem):
        """
        Adds the elem to one end of the containre list, keeping the end you add to consistent.
        Does not return anything
        """
        # your code here
        self.element = elem

        self.myList.append(self.element)

class Stack(Container):
    """ 
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The newest element in the containre list is removed 
        Returns the elmeent removed or None if the queue contains no elements 
        """
        # your code here
        if self.size() > 0: # if the len of myList is more than 0 , we remove the list until its None. Maybe we add __str__ method to print the correct sentence
            return self.myList.pop()
        return None
        # we can use inheritance from Container class

myList = Container()
myList.add(["abc","bcd"]) #still counted as 1 element
print(myList.size())
myStack = Stack()
myStack.add({"asepak": 25, "burangrang": 35})
print(myStack)
print(myStack.remove())



