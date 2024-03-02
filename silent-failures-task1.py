#You are provided with a Python script that is supposed to handle
#errors silently, but it has some mistakes. Identify and fix them.

'''
Buggy code:
try:
    x = 1 / 0
except ZeroDivisionError
    pass
'''

try:
    x = 1 / 0
except ZeroDivisionError:   #added a missing colon
    pass