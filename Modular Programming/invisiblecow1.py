__author__ = 'eric'
import random
import math

# welcome header
print "**********************************************"
print "* Welcome to the Find the Invisible Cow Game *"
print "**********************************************"
print " "


# get random x and y - represents the location of the invisible cow
cow_x = random.randint(0, 640)
cow_y = random.randint(0, 480)

name = raw_input("Please enter your name: ")
print "The cow is set, good luck " + name + "!!"


# initialize the found flag
found = False


# get guesses until found
while not found:
    # get a guess
    guess_x = input("Enter guess location x value: ")
    guess_y = input("Enter guess location y value: ")

    # check to see if the guess is out bounds
    if guess_x < 0 or guess_x > 640 or guess_y < 0 or guess_y > 480:
        print "Out of bounds, try again"

    else:
        # calculate the distance from the guess to the cow
        distance = abs(math.sqrt((guess_x - cow_x)**2 + (guess_y - cow_y)**2))

        # give appropriate clue based on distance
        if distance < 10:
            # cow found
            print "Yeah you found it!!"
            found = True

        elif distance < 20:
            print "MOO!!! MOO!! MOO!!"

        elif distance < 50:
            print "MOO MOO MOO"

        elif distance < 100:
            print "Moo Moo Moo"

        elif distance < 200:
            print "moo moo moo"

        elif distance < 300:
            print "moo"

        else:
            print "m"


