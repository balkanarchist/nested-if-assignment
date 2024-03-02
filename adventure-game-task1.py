# You are provided with a Python script that is supposed to guide a user
# through an adventure game, but it has some errors. Identify and fix them.


'''
Buggy code
place = input("Choose a place: forest or cave? ")
if place = "forest":
    action = input("climb a tree or cross a river?")
    if action = "climb a tree":
        print("You found a bird's nest!")
    else action = "cross a river":
        print("You found a boat!")
elif place = "cave":
    print("You find a hidden treasure!")
'''


place = input("Choose a place: forest or cave? ")


if place == "forest": #changed equal sign to equal (comparison) operator
    action = input("climb a tree or cross a river?")
    if action == "climb a tree": #changed equal sign to equal (comparison) operator
        print("You found a bird's nest!")
    else: #removed stated condition because it's an else
        print("You found a boat!")
elif place == "cave": #changed equal sign to equal (comparison) operator
    print("You find a hidden treasure!")