hour_unit = 24
minutes_unit = hour_unit * 60
seconds_unit = minutes_unit * 60


def days_to_units(number_of_days, conversion_unit):
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


def validate_and_execute(days_and_unit_dictionary):
    try:
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


user_input_message = "Hey user, enter number of days and conversion unit.\n" \
                     "Ex. 1:seconds, 2:minutes, 3:hours ...etc (days:units)\n"
