# The try block lets you test a block of code for errors.
# Except block lets you handle error.
# Else block lets you excute code when there is no error.
# The finally block let you excute the code, regradless of the result of the try- and except blocks.
# try:
#     print(x)
# except:
#     print("Somethis wrong with this code") # This will gives error, so exceptional statement print in output
# try:
#     print(x) #This will gives error , so exceptional statement print in output
# except NameError:
#     print("X is not defined") # this is name defined error
# except:
#     print("Something else is wrong")


# try:
#     print("Hello")
# except:
#     print("Something wrong with code")
# else:
#     print("Nothing wrong with code") # When there is nothing wrong with code we it execute else statement


# try:
#     print("Hello")
#     print(x)
# except:
#     print("Something wrong with code")
# else:
#     print("There is nothing wrong with code")
# finally:
#     print("This will print every time even if there is error or not")


# try:
#     f = open("story.txt")
#     try:
#         f.write("Lorem i;laks")
#     except:
#         print("Something wrong with this file")
#     finally:
#         f.close()
# except:
#     print("Something went wrong when opening the file")

# Raise Keyword

# x = -1 

# if x < 0:
#     raise Exception("Sorry, no is less than zero ")

x  = "Hello"
if not type(x) is int:
    raise Exception("Only integer is allowed")

