# Standalone Build-In function

# - Prints to the standard output device
print("Prints to the standard output device\n")

# - Ask user for input
input("Enter value")

# - Return a new set
set([1, 3, 4])

# - Converts value into an integer number
int("33")

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

# Build-In function on Data types
# - each data type has its own build-in functions
# - which are useful and make sense only for this specific data type.

# String (10, 22, 50, 100) -> List [10, 22, 50, 100] by using spilt().
# String - spilt() : default separator is any whitespace.
# Or it can override separator by using "," or others.
"2, 5".split()

# Return the number of non-overlapping occurrences of substring sub
# in string S[start:end].
# Optional arguments start and end are interpreted as in slice notation.
"text".count("t")
print("text".count("t"))
