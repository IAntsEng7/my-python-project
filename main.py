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


# Lists :
# 1. To store multiple items in a single variable.
# 2. A list can contain different data type.
user_input = ""
while user_input != "exit":
    user_input = input(
        "Hey user, \n"
        "enter number of days as a comma separate list, \n"
        "and I wii convert it to hours.\n"
        "Or text exit to end this program.\n")
    print(type(user_input.split(",")))
    print(user_input.split(","))
    # For Loop :
    # It's used for iterating over a sequence (like a list).
    # So we can execute smth for each item in a list.

    # String (10, 22, 50, 100) -> List [10, 22, 50, 100] by using spilt().
    # String - spilt() : default separator is any whitespace.
    # Or it can override separator by using ",".
    for number_of_days_element in user_input.split(","):
        validate_and_execute()
