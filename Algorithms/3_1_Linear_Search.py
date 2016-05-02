__author__ = 'eric'

import random

def example1():

    # generate a random list of integers
    numlist = []

    for i in range(10):
        numlist.append(random.randint(1, 100))

    # prompt user for a value
    key = input("Choose a number between 1-100: ")

    # search for value using linear search

    index = 0
    location = -1

    while index < len(numlist):
        if numlist[index] == key:
            location = index
            break
        else:
            index += 1

    print numlist
    if location != -1:
        print "You guessed right!! It is in position", location
    else:
        print "You guessed wrong.  Your number is not in the list"



def example2():

    # generate a random list of passwords
    plist = []

    for i in range(5):
        plist.append(raw_input("Enter a password: "))

    # prompt user for a value
    key = raw_input("Enter a NEW password: ")

    # search for value using linear search

    index = 0
    location = -1

    while index < len(plist):
        if plist[index] == key:
            location = index
            break
        else:
            index += 1

    print plist
    if location != -1:
        print "You've entered an existing password.  Enter a new one"
    else:
        print "Your password has been reset"


