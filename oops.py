# Inheritance Concept
# Inheritance allows us to define a class that inherits all the methods and proparities from another class.
# Parent class is the class being inherited from, also caled base class.
# Child class is the class that inherits from another class, also called derived class.

class Teacher:
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName

    def printName(self):
        print(self.fName, self.lName)
    
class Student(Teacher):
    pass # We use pass when we don't want to pass any method or other values in class
x = Student("Smit", "Prajapati") # As we can see Student inherits all properties from Teacher
x.printName()