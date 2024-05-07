# Inheritance Concept
# Inheritance allows us to define a class that inherits all the methods and proparities from another class.
# Parent class is the class being inherited from, also caled base class.
# Child class is the class that inherits from another class, also called derived class.

# class Teacher:
#     def __init__(self, fName, lName):
#         self.fName = fName
#         self.lName = lName

#     def printName(self):
#         print(self.fName, self.lName)
    
# class Student(Teacher):
#     pass # We use pass when we don't want to pass any method or other values in class
# x = Student("Smit", "Prajapati") # As we can see Student inherits all properties from Teacher
# x.printName()
# Python has super() keyword that will make the child(derived class) class inherit all the methods and properties from its parent(base class)

# class Student(Teacher):
#     def __init__(self, fName, lName, year):
#         super().__init__(fName, lName)
#         self.graduatinYear = year

# x = Student("Smit", "Prajapati", 2023)
# print(x.graduatinYear)

# print(x)


# Iterators in Python

# A Iterator is object that content countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

# myTup = ("mv", "tv", "av")
myTup = ("smit")

myIt = iter(myTup)
print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))
