'''
You are provided with a Python script that is supposed to monitor system parameters, but it has some mistakes. Identify and fix them.

Buggy Code:

import random

cpu_usage = random.randint(0, 100)
if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90
    pass
'''

import random

cpu_usage = random.randint(0, 100)
if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90:    #appended colon to end of elif
    pass