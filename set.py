# User input : 33, 1, 33
# console:
# 33 days are 792 hours
# 1 day is 24 hours
# 33 days are 792 hours
# If user type the same number, we want to compile it one time.


calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(number_of_days):
    if number_of_days == 1:
        return f"{number_of_days} day is " \
               f"{number_of_days * calculation_to_units} {name_of_unit}"
    elif number_of_days > 0:
        return f"{number_of_days} days are " \
               f"{number_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(number_of_days_element)
        if user_input_number > 0:
            calculation_value = days_to_units(user_input_number)
            print(calculation_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number.")
        elif user_input_number < 0:
            print("You entered a negative number, no conversion for it.")
    except ValueError:
        print("Your input is not a valid number. Don't ruin my program.")


user_input = ""
while user_input != "exit":
    user_input = input(
        "Hey user, \n"
        "enter number of days as a comma separate list, \n"
        "and I wii convert it to hours.\n"
        "Or text exit to end this program.\n")
    list_of_days = user_input.split(", ")
    # set()
    # - another build-in data type of Python.
    # - as with Lists, used to store multiple items of data.
    # - does "NOT" allow duplicate value.

    # Ex. user type in : 1,3,5,3,7,1,3,5,9
    print(list_of_days)
    # console : ['1,3,5,3,7,1,3,5,9']
    print(type(list_of_days))
    # console : <class 'list'>

    print(set(list_of_days))
    # console : {'1,3,5,3,7,1,3,5,9'}
    print(type(set(list_of_days)))
    # console : <class 'set'>

    for number_of_days_element in set(list_of_days):
        validate_and_execute()
