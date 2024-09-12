class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initializes an empty list
        """
        self.myList = []

    def size(self):
        """
        Returns the length of the container list
        """
        # Your code here
        length = len(self.myList)
        return length

    def add(self, elem):
        """
        Adds the elem to one end of the container list, keeping the end
        you add to consistent. Does not return anything
        """
        # Your code here
        self.myList.append(elem)

    def __str__(self):
        return f"{self.myList} (length: {self.size()})"

class Queue(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The oldest element in the container list is removed
        Returns the element removed or None if the stack contains no elements
        """
        # using pop method
        if self.size() > 0:
            return self.myList.pop(0)
        else:
            return None

test = Container()
test.add("babuga")
print(test)
test1 = Queue()
test1.add("apple")
print(test1)
test1.remove()
print(test1)