# In Python file handeling is important part of web applicatin
# Python has several function to creating, reading, updating, and deleting `file`s.

# The key function working with files in python is the open() function.
# The open function takes two parameters: filename and mode.
# # There are four different methods (modes) for opening files.
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

# f = open("currencyData.txt", "a") # When file is locate in different we use D:\\myfiles\currencyData.txt

# print(f.read()) # With this we can read the file in terminal
# print(f.readline()) # It return fist line of text from file and if you gives two readLine it returns first two line from it

# for x in f:
#     print(x)

# print(f.read())

# f.close() # With the help of close() it will stop to read or do other thing for this file
# print(f.read())

# f.write("how are you guys, THis text will add in currencyData")
# f.close()

# f = open("currencyData.txt", "r")
# print(f.read())

# f = open("currencyData.txt", "w")
# # With "w" it delets all the data from text file
# f.write("oops!, I delete all text")
# f.close()

# f = open("currencyData.txt", "r")
# print(f.read())

# m = open("myText.txt", "x")
# m.close()
# m = open("myText.txt", "w")
# m.write("Hey how are you")
# print(m)

import os # With ths help os os module and remove function we can remove file

# os.remove("myText.txt")

# if os.path.exists("file.txt"):
#     os.remove("file.txt")
# else:
#     print("File doesn't exit")

os.rmdir("currency_convert") # With the help of rmdir we can delete whole folder