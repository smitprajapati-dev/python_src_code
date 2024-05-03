# Dictionary is of four data type, it always works on key:value pair. In new python version(3.7) dictionay is ordered but, in 3.6 it was unordered. We can change value of dictionary, but we can't create dublicate


dic = {
    "sureName": "Prajapati",
    "FirstName":"Smit",
    "birthYear":2002 
}
# This is how we creates dictionary
# To access
print(dic["FirstName"])
print(dic.get("birthYear")) # With the help of get() we can get perticular key's value. 
# Dictionary's is always comes with key and value so we can access with it.
# x = dic.keys()
# dic["cars"] = "celario"
# print(x)

# print(dic.values())
# we can change value of dictionary with the help of update() and it is also use to add value
dic.update({"sureName" : "King"}) # You have to write new value in {}
dic.update({"middleName" : "Kanubhai"})
print(dic)


