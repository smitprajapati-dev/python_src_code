# To create tuple you can write multiple variable in () for example
# Tuples are always in order, we can create dublicate and it is immutable(means we can't change value of tuple)
# tp = ("smit","prajapati", "sounu", "Kanubhai")
# print(tp[-1])
# print(tp[1:3])

# Tuple are immutable so, to change value, first of all you have to change tuple into list and than after you can chane value of if and than you can convert back into tuple.For example

tupl = ("smit", "sonu", "prajapati")
li = list(tupl)
li[1] = "Ro"
tupl = tuple(li)

print(tupl)


