# You are provided with a Python script that is supposed to help in event planning, but it has errors.
# Identify and fix them. // This is a shorthand practice exercise.

'''
attendees = input("Enter number of attendees: ")
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
'''

attendees = int(input("Enter number of attendees: ")) # needed to convert input to an integer
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# The code tested well. If there are other errors, I don't see them.