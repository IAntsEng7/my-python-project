import math
from datetime import datetime, timezone
import os
import logging

# math
print(math.pow(2, 6))
# 64.0
print(math.sqrt(25))
# 5.0
print(math.floor(5 / 2))
# 2
print(math.ceil(5 / 2))
# 3

# datetime
# - datetime module provides many functions that
#   make it easier to work with dates and times.
now = datetime.now()
print(now)
my_timezone = timezone.utc
print(my_timezone)

# os
print(os.name)
print(os.path)

# logging
logger = logging.getLogger("MAIN")
logger.error("Error happened in the app.")
