# If the user makes an invalid choice at any point, use the pass statement for now. Later,
# you can enhance this to provide feedback or a different branch of the story.


place = input("Choose a place: forest or cave? ")


if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You see a colony of bats coming back at you!")
    else:
        print("Fumble around until you find a nasty looking light switch.")
else:    
    print("You find a hidden treasure!")


# still need to add pass statement
