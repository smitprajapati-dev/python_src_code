# A function is block of code it will only execute when it called.
# You can pass date in parameters, into a function.
# A function can return data as a result


# def fun(): # This is simple functin.
#     print("This is function")

# fun()


# def my_fun(fName):
#     print(f"My name is {fName} ")

# my_fun("smit") # There is one catch, when ever we pass 2 or multiple parameters in function we must pass same number of argument in function declaration.

# my_fun(fName="Sonu") # you can also give argument like this

# def func(**kid):
#     print("This kid name is")
# func(fname= "Smit" ,lname="Prajapati") # **kid passed because we don't know how many parameters is passed in decalation of fuction

def my_fun(name="Smit"): # Like this we can pass default parameters
    print(f"My name is {name}")

my_fun()

