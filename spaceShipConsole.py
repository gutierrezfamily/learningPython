import time
shipName = "The Dragonflight"
captain = raw_input("What is your name?: ")
location = "Titan, one of Saturn's moons"
password1 = "TheGasterBlasterMasterismyDadster"
password2 = "*noises of excitement and death*"

pAttempt = raw_input("Enter the password: ")
while pAttempt != password1:
    print "Password incorrect"
    pAttempt = raw_input("Enter the password: ")
print "Password correct. Welcome to the " + shipName + ", captain!"

print " "
print "[Captain's Log, 20XX]"
print "[The galaxycruiser '" + shipName + "' is currently refueling at \n" + location + ".]"

choice = " "
while choice != "/exit":
    print "What would you like to do, " + captain + "?"
    print " "
    print "a. Travel to another planet"
    print "b. Fire cannons"
    print "c. Open the airlock"
    print "d. Self-destruct"
    print "/exit to exit"
    print " "
    choice = raw_input ("Enter your choice: ")

    if choice == "a":
        destination = raw_input("Where would you like to go? ")
        print "All hands on deck! Prepare for liftoff!"
        print "Leaving " + location
        print "Travelling to " + destination
        time.sleep(5)
        print "Arrived at " + destination
        location = destination
     
    elif choice == "b":
        print "Firing cannons"
        time.sleep(1)
        again = "yes"
        while again == "yes":
            choice2 = raw_input("Select Target: \n a. space rocks \n b. alien invaders \n c. innocent spacemen in their ship \n Target: ")
        
            if choice2 == "a":
                print "KABOOM! No more space rocks."
                
            elif choice2 == "b":
                print "BLAM BLAM! Galaxy saved!"
                
            elif choice2 == "c":
                print "Oh no! You've murdered them!"
                
            else:
                print "That's not a target. Please select a target. \n /exit to exit."
            again = raw_input( "Wanna blast some more things? \n Answer: ")
    elif choice == "c":
        print "Opening airlock"
        time.sleep(3)
        print "Airlock open"
        time.sleep(1)

    elif choice == "d":
        confirm = raw_input("Are you sure you want the ship to self-destruct? \n (y/n)")
        if confirm == "y":
              pAttempt2 = raw_input("Please confirm self-destruct password: ")
              while pAttempt2 != password2:
                  print "Password incorrect. Access denied."
                  pAttempt2 = raw_input("Please confirm self-destruct password: ")
        print "Ship will self-destruct in"
        print "3"
        time.sleep(1)
        print "2"
        time.sleep(1)
        print "1"
        time.sleep(1)
        print "Goodbye."
        time.sleep(3)
        print "B O O M !"
        choice = "/exit"

    elif choice == "/exit":
        print "Goodbye"

    else:
        print "Invalid input. Please select a, b, c, or d. \n /exit to exit"
