__author__ = 'eric'
import math
import random

def showWelcomeHeader():
    """
    Display the welcome header
    :return: None
    """

    # welcome header
    print "**********************************************"
    print "* Welcome to the Find the Invisible Cow Game *"
    print "**********************************************"
    print ""

def showStatus(zone):
    """
    Output the appropriate clue based on zone
    :param zone: int - the calculated zone of the guess
    :return:None
    """

    if zone == 1:
        print "Yeah! You found it!"

    elif zone == 2:
        print "MOO!!! MOO!! MOO!!"

    elif zone == 3:
        print "MOO MOO MOO"

    elif zone == 4:
        print "Moo Moo Moo"

    elif zone == 5:
        print "moo moo moo"

    elif zone == 6:
        print "moo"

    else:
        print "m"

def get_distance(x1,y1,x2,y2):
        """
    Compute the distance between two points
    :param x1: int - point 1 x
    :param y1: int - point 1 y
    :param x2: int - point 2 x
    :param y2: int - point 2 y
    :return: float - computed distance
    """

    inner = (x2 - x1)**2 + (y2 - y1)**2
    return math.sqrt(inner)

def isOutofBounds(x, y, maxX, maxY):
    """
    check to see if player's guess is within the boundaries
    :param x: int - player x
    :param y: int - player y
    :param maxX:  - maximum x
    :param maxY:  - maximum y
    :return: boolean
    """

    return x < 0 or y < 0 or x > maxX or y > maxY

def getPlayerXY():

    # get the x y inputs from the user
    player_x = input("Enter an x value:  ")
    player_y = input("Enter a y value:  ")

    # check of the player xy is out of bounds
    while isOutofBounds(player_x, player_y, 640, 480):
        print "Out of bounds values specified. Stay within 640x480"

        # get the x y inputs from the user
        player_x = input("Enter an x value:  ")
        player_y = input("Enter a y value:  ")

    return player_x, player_y

def getzone(playerX, playerY, cowX, cowY):

    distance = get_distance(playerX, playerY, cowX, cowY)

    if distance < 10:
        return 1

    elif distance < 20:
        return 2

    elif distance < 50:
        return 3

    elif distance < 100:
        return 4

    elif distance < 200:
        return 5

    elif distance < 300:
        return 6

    else:
        return 7

def get_cow_xy():

    cow_x = random.randint(0,640)
    cow_y = random.randint(0, 480)

    return cow_x, cow_y

def main():
    """
    Main executable program
    :return: None
    """

    # show the welcome
    showWelcomeHeader()

    # generate the cow
    c_x, c_y = get_cow_xy()

    # get player xy until cow is found
    found = False

    while not found:
        player_x, player_y = getPlayerXY()

        zone = getzone(player_x, player_y, c_x, c_y)
        showStatus(zone)
        if zone == 1:
            found = True

main()

