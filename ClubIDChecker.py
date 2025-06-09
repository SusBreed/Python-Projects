import time

print("Chelsea: Welcome to Breeze Club! ")
time.sleep(1)
print("Chelsea: Before we enter the club we'll need to make you an ID! ")
time.sleep(3)

idchecker = (input("ID Maker: How old are you? "))
while not idchecker.isdigit():
    idchecker = (input("ID Maker: How old are you? "))
age = int(idchecker)
time.sleep(2)
print("Now that we have your ID ready, lets head to the Breeze Club! ")
time.sleep(2)

print("Security Guard: Hi, I'll need to see some ID... ")
time.sleep(2)

while True:
    Security_Guard = input("Hand over your ID? Yes/No ").lower()

    if Security_Guard == "yes":
        time.sleep(1)
        print("Security Guard: Alrighty, lets take a look here... ")
        break
    elif Security_Guard == "no":
        print("Sorry you won't be allowed inside. ")
        time.sleep(1)
        print("I'm going to have to ask you to leave.")
        time.sleep(2)
        print("Game Over.")
        exit()
    else:
        print("Invalid response. Please type 'Yes' or 'No'. ")
        time.sleep(1)

if age >= 18:
    time.sleep(3)
    print("Security Guard: You are of age, enjoy your time in Breeze Club! ")
    exit()
elif age <=17:
    print("Security Guard: You are too young and must leave. ")
    time.sleep(3)
Run = input("Will you attempt to run past Security? Yes/No ").lower()
if Run == ("yes"):
    time.sleep(3)
    print("You got past the 1st guard but there were more inside! ")
    time.sleep(3)
    print("The guards grabbed you & kicked you out! ")
    time.sleep(2)
    print("Game Over. ")
    exit()
elif Run == ("no"):
    print("Good choice, come back when you're older! ")
    exit()