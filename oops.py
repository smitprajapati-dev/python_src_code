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
# myTup = ("smit")

# myIt = iter(myTup)
# print(next(myIt))
# print(next(myIt))
# print(next(myIt))
# print(next(myIt))


# Polymorphism
# The word polymorphism means "many form", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classis.

# myTup = ("Smit", "Prajapati", "Sonu")
# myList = ["Sonu", "Smit"]
# myDict = {"name":"smit",
#           "age":21
#           }
# # len() is function polymrophism because we can use many time
# print(len(myTup))
# print(len(myList))
# print(len(myDict))


# Class polymorphism
# Polymorphism is often used in class methods, where we can have multiple classes wiht the same methods name.
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():


# class Car:
#     def __init__(self, brand, model) :
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Drive")
# class Boat:
#     def __init__(self, brand, model) :
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Serf")

# class Plane:
#     def __init__(self, brand, model) :
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Fly")

# car1 = Car("Suzuki", "Celerio")
# boat1 = Boat("Honda", "yaht")
# plane1 = Plane("IndianFly", "Sukoi")

# for x in (car1, boat1, plane1):
#     x.move()
# print(car1, boat1, plane1)


# Inheritance Class Polymorphism

# What about classes with child classes with the same name? Can we use polymorphism there?

# Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move")

class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("Serf")

class Plane(Vehicle):
    def move(self):
        print("Fly")
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boing", "Sukoi")

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

# Child classes inherits the properties and methods from the parent class.
# In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.
# The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.

# Because of polymorphism we can execute the same method for all classes.