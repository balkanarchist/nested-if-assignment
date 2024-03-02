'''
Ask the user if they want "vegetarian" food.
Recommend "Veggie Delight Caterers" if yes,
otherwise recommend "Gourmet Meals Caterers".
'''

attendees = int(input("Enter number of attendees: "))

venue = "large hall" if attendees > 100 else "conference room"
print(venue)

    
if attendees > 100:
    print("I recommend using a sound system for large venues such as this.")
else:
    print("I recommend using a projector for smaller venues such as this.")

meal_service = input("Would you like vegetarian food? (yes/no): ")
if meal_service == "yes":
    print("Then I recommend Veggie Delight Caterers.")
elif meal_service == "no":
    print("Then I recommend Gourmet Meals Caterers.")
else:
    print("Please type yes or no for vegetarian food.")