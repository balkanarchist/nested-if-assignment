'''
Based on the corrected code from Task 1, further enhance the program
to recommend additional facilities like "audio system" or
"projector" based on the number of attendees.
'''

attendees = int(input("Enter number of attendees: "))

venue = "large hall" if attendees > 100 else "conference room"
print(venue)

    
if attendees > 100:
    print("I recommend using a sound system for large venues such as this.")
else:
    print("I recommend using a projector for smaller venues such as this.")