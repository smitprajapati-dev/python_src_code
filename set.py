# # To create set we gives value in {} 
# # set is immutable, unorder, and we can't dublicate it 
# # unorder means items do not have defined order

# st = {"smit", "prajapati"}
# # print(st[1]) You can't access set with this synatax to access we heve to...

# print("smit" in st) 

# # Set is unchangable(immutable) but, we can add items

# st.add("Sonu")
# print(st)

# # To combine two set we use update()

# st1 = {"smit", 12,212,563}
# st2 = {33,36,72}
# # st1.update(st2)
# lit = ["smit",333]
# st1.update(lit) # We can also combine list and set or others like tuple and dictionary
# print(st1)

st = {213,32,132,311,72}
st.remove(32) # It removes targeted item
st.discard(213) # It works same as remove(), but when an item do not exit in set it will rise an error
st.pop() # pop() randomly remove item from set
st.clear() # clear() will remove all the items from set
del st # del will delete whole set from program


# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns whether another set contains this set or not
#  	<	Returns whether all items in this set is present in other, specified set(s)
# issuperset()	>=	Returns whether this set contains another set or not
#  	>	Returns whether all items in other, specified set(s) is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others
