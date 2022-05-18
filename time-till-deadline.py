# import datetime
from datetime import datetime

# Let user input their goal and date or deadline to the goal.
user_input = input(
    "Please enter your goal with a deadline(mm.dd.yyyy) separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
print(input_list)

# String -> datetime, strptime(variable, format)
# deadline_date = datetime.datetime.strptime(deadline, "%m.%d.%Y")
# print(datetime.datetime.strptime(deadline, "%m.%d.%Y"))
deadline_date = datetime.strptime(deadline, "%m.%d.%Y")
print(datetime.strptime(deadline, "%m.%d.%Y"))
# first datetime is module, second datetime is function in datetime module.

# calculate how many days from now till deadline
# today_date = datetime.datetime.today()
today_date = datetime.today()

time_till = deadline_date - today_date

print(
    f"Dear user! Time remaining for your goal: {goal} is "
    f"{time_till.days} days.")

hours_till = time_till.total_seconds() / 60 / 60
print(
    f"Dear user! Time remaining for your goal: {goal} is "
    f"{int(hours_till)} hours.")
