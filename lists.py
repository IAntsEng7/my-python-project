# Basic list operation :
# - Create a list.
my_list = ["January", "February", "March"]
# - list.length
print(f"My list length is {len(my_list)}")
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
# - Add an item to the list.
my_list.append("April")
print(my_list)
# - Remove an item from the list.
my_list.remove("January")
print(my_list)
# - Change items in the list.
my_list[0] = "January"
my_list[-1] = "May"
print(my_list)
# - Access items of the list by using for loop
for i in my_list:
    print(i)
