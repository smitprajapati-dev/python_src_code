# class is also called object in python
# Python is object oriented programming language
# Almost everything in python is an object, with its properties and methods.
# A class is like an object constructor, or a "blueprint" for creating object.
# Creating class is simple
# always use first word capital to create class
class MyClass :
    x = 5

p1 = MyClass() # When we want to display value from class we have to create instance like this
p1.x = 11 # we can also modified the properties of object
del p1.x # with this we can delete the properties and also we can delete whole object 
print(p1.x)
#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"My name is {self.name} and my age is {self.age}"
        
p1 = Person("smit", 21)    
print(p1.age)
# print(p1.name)
# print(p1.age)
# The __init__() function is called automatically every time the class is being used to create a new object.