# Adventure Quest

import time

print("Welcome to Adventure Quest!!")
time.sleep(1)

name = input("What is your name traveler? ")
while not name.isalpha():
    name = input("What is your name? ")
time.sleep(2)

print("Hello " + name + ", let's begin our quest! ")
time.sleep(2)

while True:
    weapon = input("Would you like a sword or pistol? ").lower()
    if weapon == "sword":
        time.sleep(2)
        print("Great! Your sword does 4 damage!")
        time.sleep(2)
        break
    elif weapon == "pistol":
        time.sleep(2)
        print("Awesome! Your pistol does 4 damage!")
        time.sleep(2)
        break
    else:
        print("Invalid response. Try again.")
        time.sleep(1)

continue_game = input("Now that you've chosen your weapon, would you like to continue our adventure? Yes/No ").lower()
    
if continue_game == "yes":
    print("Alright, let's continue!")
    time.sleep(2)
elif continue_game == "no":
    print("Alright, have a great day!")
    time.sleep(2)
    exit()
else:
    print("Invalid response. Try again.")
    exit()

print("A monster has appeared with 8 HP!")
time.sleep(2)

while True:
    if weapon == "sword":
        action = input("With two swings of your sword, you can kill the monster! Will you swing? Yes/No ").lower()
    elif weapon == "pistol":
        action = input("With two shots of your pistol, you can kill the monster! Will you shoot? Yes/No ").lower()

    if action == "yes":
        print("You have slain the beast!!")
        time.sleep(2)
        break
    elif action == "no":
        print("You hesitated... and the monster ate you. Game over.")
        time.sleep(2)
        exit()
    else:
        print("Invalid response. Try again.")
        time.sleep(1)

print("Congratulations adventurer!!")
exit()