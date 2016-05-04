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


def birthdayMatch (maxPartySize):
    """
    Checks if a birthday match exists within a group of size maxPartySize
    param: maxPartySize: int - the size of the group of people to test.
    return: boolean - True if match found
    """

    birthday_list = []
    for i in range(maxPartySize):
        new_person = random.randint(0, 364)

        # a linear search
        for i in range(len(birthday_list)):
            if birthday_list[i] == new_person:
                return True

        birthday_list.append(new_person)

    return False

def main():
    num_test = 10000
    count = 0

    for i in range(num_test):
        if birthdayMatch(30):
            count += 1

    print count/float(num_test)

main()



