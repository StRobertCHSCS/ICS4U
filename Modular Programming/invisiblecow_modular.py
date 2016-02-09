__author__ = 'Eric Fabroa'
#-------------------------------------------------------------------------------
# Name:	invisiblecow_modular.py
# Purpose:
# A commandline version of the popular Find the Invisible Cow Game
#
# Author:	Fabroa.E
#
# Created:	09/02/2016
#-------------------------------------------------------------------------------


import math
import random

def showWelcomeHeader():
    """
    Display welcome header
    :return: None
    """

    # welcome header
    print "**********************************************"
    print "* Welcome to the Find the Invisible Cow Game *"
    print "**********************************************"
    print ""

def showStatus(zone):
    """
    Display the appropriate status based on a given zone
    :param zone: int - zone where the player guess resides
    :return: None
    """

    if zone == 1:
        print "Yeah you found it!!"

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
    Calculate the distance between two points
    :param x1: int - point 1 x value
    :param y1: int - point 1 y value
    :param x2: int - point 2 x value
    :param y2: int - point 2 y value
    :return: float - the computed distance
    """

    inner = (x2 - x1)**2 + (y2-y1)**2
    return math.sqrt(inner)

def isOutofBounds(x,y,maxX,maxY):
    """
    Determine if a given point is within a given boundary
    :param x: int - player x value
    :param y: int - player y value
    :param maxX: int - max x value
    :param maxY: int - max y value
    :return: boolean
    """

    return x<0 or x> maxX or y<0 or y>maxY

def getPlayerXY():

    # prompt the player for x and y values
    playerX = input("Enter an x value: ")
    playerY = input("Enter a y value: ")

    while isOutofBounds(playerX,playerY, 640,480):
        print "You have entered an out of bound point. Please enter values within a 640x480 space."

        # prompt the player for x and y values
        playerX = input("Enter an x value: ")
        playerY = input("Enter a y value: ")

    return playerX, playerY

def getZone(playerX, playerY, cowX, cowY):

    # compute distance
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

    x = random.randint(0,640)
    y = random.randint(0,480)

    return x, y


def main():

    # show the welcome
    showWelcomeHeader()

    # generate invisible cow
    cow_x, cow_y = get_cow_xy()

    #repeat until found
    found = False

    while not found:
        # get the player x,y
        player_x, player_y = getPlayerXY()

        # get zone
        zone = getZone(player_x, player_y, cow_x, cow_y)

        # show the status
        showStatus(zone)

        if zone == 1:
            found = True

main()