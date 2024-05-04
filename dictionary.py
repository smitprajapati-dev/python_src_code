# Dictionary is of four data type, it always works on key:value pair. In new python version(3.7) dictionay is ordered but, in 3.6 it was unordered. We can change value of dictionary, but we can't create dublicate


dic = {
    "sureName": "Prajapati",
    "FirstName":"Smit",
    "birthYear":2002 
}
# This is how we creates dictionary
# To access
# print(dic["FirstName"])
# print(dic.get("birthYear")) # With the help of get() we can get perticular key's value. 
# Dictionary's is always comes with key and value so we can access with it.
# x = dic.keys()
# dic["cars"] = "celario"
# print(x)

# print(dic.values())
# we can change value of dictionary with the help of update() and it is also use to add value
# dic.update({"sureName" : "King"}) # You have to write new value in {}
# dic.update({"middleName" : "Kanubhai"})
# print(dic)

# To remove items from dictionary there are different ways
# dic.pop("sureName") # It removes items from specific place
# dic.popitem() # It removes last item from index(dictionary)
# dic.clear() # It clears whole dictionary
# print(dic) 

# and to del entire dictionary we use del
# del dic

# To create copy we use copy() and another way to create copy is dict()

dic1 = dic.copy()
dic2 = dict(dic)

print(dic2)


# Ther are others methods in dictionary

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary
