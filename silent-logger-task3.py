'''If any of the system parameters exceed a certain threshold, print an alert message.
However, if the system parameter is within a "gray zone", use the pass statement to
silently log this without alerting the user.
'''

import random

cpu_usage = random.randint(0, 100)
if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90:
    pass

memory_usage = random.randint(0, 100)
if memory_usage > 85:
    print("High memory usage!")
elif memory_usage > 75 and memory_usage <=85:
    pass

disk_space = random.randint(0, 100)
if disk_space > 90:
    print("High disk space usage!")
elif disk_space > 50 and disk_space <= 90:
    pass