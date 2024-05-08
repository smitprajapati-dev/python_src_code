# # In python there is scope concept like others programming language 
# x = 12 # This is global scope so you can access this variable everywhere, in function or outside the function
# def myFun(): # This is function scope, means you can only access properties of function in function, and you can't access outsite of function's properties
#     x = 10
#     print(x)

# print(x)

# def myFun():
#     global x # With global keyword inside function you can declare globale variable
#     x = 100

# print(x)

# x = 300

# def myfunc():
#   global x # This value will apply globaly now, even if it has same variable declared at the outside of function  it gives this value
#   x = 200

# myfunc()
# x = 120 # And if you declare after it give this value
# print(x)

# Nonlocal Keyword:- The nonlocal keyword is used to work with variables inside nested functions. The nonlocal keyword makes the variable belong to the outer function.

def outer():
    x = "june"
    def inside():
        nonlocal x
        x = "hello"
    inside()
    return x

print(outer())