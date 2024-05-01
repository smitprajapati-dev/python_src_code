# # To create list we store value in [] 
# # List are always in order, it changable, and it can be dublicated
# li = ["smit", "Prajapati"]

# print(len(li)) # To find list length you can use len()
# # It can store different value such as int, float, or string
# list1 = ["smit", 23.3, 22, 23,42,45,11]
# print(list1)
# print(type(list1)) # to check data type you can write list1

# print(list1[1]) # with this you can access list items and it always starts with 0
# print(list1[-1]) # You can also use negative to access value
# print(list1[0 : 5])
# print(list1[-1: -5])

# list1[1: 3] = ["Kong", "Godzilla", "Range"] # with this you can also modifie list
# list1.insert(1, "king_kong") # with the help of inset() you can add item in place of where you targeted
# list1.append("sonu") # with the help of append you can add item or number at the end
# print(list1)

# # to combine two list we use extend()
# list2 = [23,42,123,53]
# list3 = [12,567,78,98]
# list2.extend(list3)
# # list2.remove(12) # with the help of remove() we can remove item from list
# # list2.pop(1) # pop() is syntax that with the help of that we can remove item from specific place, however if you do not dive nummber in pop() it will remove item from end
# del list2[4] # it is also use to remove item from specific place
# print(list2)

# list2.clear() # clear keyword use to clear all the list items



# list = [23,12,43,21,90]
# for i in list:
#     print(i)

# for i in range(len(list)):
#     print(list[i])


# list.sort() # sort() helps to sorts the items in list with alphabetically, ascending, by default. It is also apply in strings value.
# list.sort(reverse = True) # it sorld reverse in decending order
# print(list)

# list1 = [12,"smit", 11, "pint"]
# list2 = list1.copy() # with this you can copy the items of string
# print("this is list1 items", list1)
# print("This is list2 items",list2)
# if "smit" in list1:
#     print("Yes, its in list1")

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list