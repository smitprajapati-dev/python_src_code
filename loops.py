# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i+= 1
# For loop use in tupl, list, set, and dict. It does not have syntax like other programming language 
tup = ("Smit", "Prajapati", "Sonu")

# for x in tup  : # With this we can print full tupl(list,set, and dictionary) in sequence
    # print(x)

# for x in tup :
#     print(x)    
#     if x == "Prajapati":
#         break # Break statement use when we want loop to stop some specific index, in this case is Prajapati
for x in tup:
    if x == "Prajapati":
        continue # Continue statement use when we want to miss the a one item and continue from next one
    print(x)

for i in range(1,5): # To print particular number we can use range()
    print(i)
for j in range(2,31,6):
    print(j)


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj: # first "red"from adj execute all the y(fruits) element and its called neasted loop 
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass # pass statement use when we don't want to execute single element from loop


# for y in "Prajapati": # It is also apply in string when we want to print string every word in sequence
#     print(y)
