# Lambda function is small anonymous function.
# A lambda function can take any number of arguments, but can only have one experession.

x = lambda a,b,c : a + b * c

print(x(12,31,2))

def myFun(n):
    return lambda a : a * n

myDoub = myFun(4)
myDub = myFun(3)
print(myDub(3))

print(myDoub(11))
