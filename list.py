# To create list we store value in [] 
# List are always in order, it changable, and it can be dublicated
li = ["smit", "Prajapati"]

print(len(li)) # To find list length you can use len()
# It can store different value such as int, float, or string
list1 = ["smit", 23.3, 22, 23,42,45,11]
print(list1)
print(type(list1)) # to check data type you can write list1

print(list1[1]) # with this you can access list items and it always starts with 0
print(list1[-1]) # You can also use negative to access value
print(list1[0 : 5])
print(list1[-1: -5])

list1[1: 3] = ["Kong", "Godzilla", "Range"] # with this you can also modifie list
list1.insert(1, "king_kong") # with the help of inset() you can add item in place of where you targeted
list1.append("sonu") # with the help of append you can add item or number at the end
print(list1)

# to combine two list we use extend()
list2 = [23,42,123,53]
list3 = [12,567,78,98]
list2.extend(list3)
# list2.remove(12) # with the help of remove() we can remove item from list
# list2.pop(1) # pop() is syntax that with the help of that we can remove item from specific place, however if you do not dive nummber in pop() it will remove item from end
del list2[4] # it is also use to remove item from specific place
print(list2)

list2.clear() # clear keyword use to clear all the list items
