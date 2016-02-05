__author__ = 'eric'
"""
filename:       invisiblecow2.py
Description:    A command line version of find the invisible cow implemented modularly using functions
Author:         E.Fabroa
"""


def showWelcomeHeader():
    """
    Show a welcome message to the screen
    :return: None
    """

    # welcome header
    print "**********************************************"
    print "* Welcome to the Find the Invisible Cow Game *"
    print "**********************************************"
    print ""

def goodLuck(playerName):
    """
    Wish the player good luck
    :param playerName: String
    :return: None
    """
    print "The cow is set, good luck " + playerName + "!!"

def get_distance(x1,y1, x2, y2):
    """
    Calculate the distance between points x1,y1 and x2,y2
    :param x1: float - x value for first coordinate
    :param y1: float - y value for first coordinate
    :param x2: float - x value for second coordinate
    :param y2: float - y value for second coordinate
    :return: float - distance between points
    """
    dist = abs(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    return dist

def isFound(distance):
    """
    Given a distance, print the appropriate message and return found status
    :param distance: distance between points
    :return: boolean - status True if found, False otherwise
    """
    if distance < 10:
        print "Found it!!"
        return True
    else:
        if distance < 20:
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

        return False

def get_cow_xy():
    """
    generate the random x and y location of the cow
    :return: int, int - cowx, cowy
    """
    x = random.randint(0, 640)
    y = random.randint(0, 480)
    return x, y

def isOutOfBounds(gx,gy):
    """
    Check to see of the given gx,gy point is within a 640x480 space
    :param gx: int - x value of the guess
    :param gy: int - y value of the guess
    :return: boolean
    """

    return gx < 0 or gx > 640 or gy < 0 or gy > 480


def main():
    """
    main executable program
    :return: None
    """
    showWelcomeHeader()

    # get random x and y - represents the location of the invisible cow
    cow_x, cow_y = get_cow_xy()

    name = raw_input("Please enter your name: ")
    goodLuck(name)

    # initialize the found flag
    found = False

    # get guesses until found
    while not found:
        # get a guess
        guess_x = input("Enter guess location x value: ")
        guess_y = input("Enter guess location y value: ")

        # check to see if the guess is out bounds
        if isOutOfBounds(guess_x,guess_y):
            print "Out of bounds, try again"
        else:
            # give appropriate clue based on distance
            found = isFound(get_distance(cow_x,cow_y, guess_x, guess_y))

main()
