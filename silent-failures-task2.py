'''
Based on the corrected code from Task 1, enhance the program
to handle other potential errors, such as ValueError when
trying to divide a number by a string.
'''

try:
    x = 1 / 0
except ZeroDivisionError:
    pass

x = int(input("Enter a number: "))
y = (input("Enter another number: "))

try:
    result = x / y
except TypeError:
    pass