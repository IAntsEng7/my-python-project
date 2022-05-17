# Basic set operation
# - Create a set
my_set = {"January", "February", "March"}

# Unordered and unchangeable -
# items is a set do not have a defined order.
# items can not be referred to by index.
# items can not be changed, only added or removed.

# Run this for loop and check the console to realized why set is unordered.
for i in my_set:
    print(i)

# - Add element
# -- The add element is just add into the set,
#    but uncertain to last or first or which place.
#    This is what items can not be referred or changed means.s
my_set.add("April")
print(my_set)

# - Remove element
my_set.remove("February")
print(my_set)
