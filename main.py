hour_unit = 24
minutes_unit = hour_unit * 60
seconds_unit = minutes_unit * 60


def days_to_units(number_of_days, conversion_unit):
    #  number_of_days -> days_and_unit_dictionary["days"]
    # conversion_unit -> days_and_unit_dictionary["units"]
    if conversion_unit == "hours":
        if number_of_days == 1:
            return f"{number_of_days} day is " \
                   f"{number_of_days * hour_unit} {conversion_unit}\n"
        elif number_of_days > 0:
            return f"{number_of_days} days are " \
                   f"{number_of_days * hour_unit} {conversion_unit}\n"
    elif conversion_unit == "minutes":
        return f"{number_of_days} days are " \
               f"{number_of_days * minutes_unit} {conversion_unit}\n"
    elif conversion_unit == "seconds":
        return f"{number_of_days} days are " \
               f"{number_of_days * seconds_unit} {conversion_unit}\n"
    else:
        return "Unsupported unit.\n"


def validate_and_execute():
    try:
        # Accessing items in a dictionary
        # - Items can be accessed by its key name.
        # - It can use square brackets or get() method.
        # -- sample_dict["days] or sample_dict.get("days")
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculation_value = days_to_units(user_input_number,
                                              days_and_unit_dictionary["unit"])
            print(calculation_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number.")
        elif user_input_number < 0:
            print("You entered a negative number, no conversion for it.")
    except ValueError:
        print("Your input is not valid. Don't ruin my program.")


# Allow user to input :
# 1. number of days, ex. 22
# 2. unit to convert to, ex. hours
user_input = ""
while user_input != "exit":
    user_input = input(
        "Hey user, enter number of days and conversion unit.\n"
        "Ex. 1:seconds, 2:minutes, 3:hours ...etc (days:units)\n")
    days_and_unit = user_input.split(":")
    # Ex. if user input "45:hours", it would spilt to "["45", "hours"]".
    print(days_and_unit)
    # Dictionary
    # used to store values in "key:value" pairs.
    # It's a collection, which doesn't allow duplicate values.
    # {"days": 20, "unit": "hours"}

    days_and_unit_dictionary = {"days": days_and_unit[0],
                                "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    # if user input is "33: hours", then console will shows :
    # ['33', 'hours']
    # {'days': '33', 'unit': 'hours'}
    validate_and_execute()
