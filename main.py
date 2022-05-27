import time

# Making a text adventure game

# Start

print("Welcome to the Text Adventure Game!")

play = input("Would you like to play? (y/n) ")

if play.lower().strip() == "y":
    print("Great! Let's get started!")

else:
    print("Okay, goodbye!")
    exit()

name = input("What is your name? ")
print("Hello, " + name + "! Let's go!")

time.sleep(1)

# Main game

print("You are in a dark room. There is a door to your right and left. Which one do you take?")
answer = input("Right or Left? ")

if answer.lower().strip() == "left" or answer.lower().strip() == "l":
    print("You decide to go left and find a door.")
    time.sleep(1)
    print("You walk through the door and find a red key.")
    redKey = True
    time.sleep(1)
    print("You find two other doors. Both are locked.")
    if redKey == True:
        print("However, you can unlock one of the doors with the red key.")
        time.sleep(1)
        answer = input("Do you want to unlock the door? (y/n) ")
        if answer.lower().strip() == "y":
            print("You go through said door.")
            time.sleep(1)
            print("You find a chest.")
            time.sleep(1)
            print("You open the chest and find a sword and a blue key.")
            time.sleep(1)
            print("You take the sword and leave the room.")
            time.sleep(1)
            print("Upon leaving the room, you find some footprints of some kind of monster.")
            time.sleep(1)
            print("You wield your sword and go to the room where you were in initially.")
            time.sleep(1)
            answer = input("Do you want to unlock the door right now? (y/n) ")
            if answer.lower().strip() == "y":
                print("You unlock the door and go through it.")
                time.sleep(1)
                print("Suddenly, a slime comes out of nowhere and attacks you.")
                answer = input("Do you want to fight or run? (f/r) ")
                if answer.lower().strip() == "f":
                    print("As it is a weak monster, you are able to defeat it.")
                    time.sleep(1)
                    print("Once you defeat the slime, you discover that there is a crate inside the slime.")
                    time.sleep(1)
                    print("You use the sword to open the crate and find a chestplate and a green key.")
elif answer.lower().strip() == "right" or answer.lower().strip() == "r":
    print("You discover that the door is actually locked.")
    time.sleep(1)
    print("However, upon further inspection, you find out the keyhole is coloured in blue.")
    time.sleep(1)
    print("You think that you can unlock the door with a blue key.")
