# Based on the corrected code from Task 1, enhance
# the program to also monitor memory usage
# and disk space, and provide alerts accordingly.

# Memory usage might be the same as cpu_usage - if not Giggle how to track it
# For disk space, same or maybe do as percentage of use

import random

cpu_usage = random.randint(0, 100)
if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90:
    pass

memory_usage = random.randint(0, 100)
if memory_usage > 85:
    print("High memory usage!")


disk_space = random.randint(0, 100)
if disk_space > 90:
    print("High disk space usage!")