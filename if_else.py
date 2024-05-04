a = 33
b = 200
if b > a:
    print("b is greater than a") #if you don't gives  a space before print you will get an error, minimum tab(  ) space is required
elif a > b:
    print("a is grater than b") # This is elif condition, when we have multiple condition we use elif

if a > b : print("a is bigger than b") # this is short way to use conditon

print("a is bigger") if a > b else print("b is bigger") # Another short way
print("a") if a > b else print("b") if a ==b  else print("b")

# When we have condition like a > b and b > c(in this condition we want two of then right) at that time we use 
if a > b and b > a: # we can also use when we want one conditon is right
    print("conditon matched") # to reverse condition we use (not a >b)

