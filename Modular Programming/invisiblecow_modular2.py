__author__ = 'eric'
import math

def showWelcomeHeader():

    # welcome header
    print "**********************************************"
    print "* Welcome to the Find the Invisible Cow Game *"
    print "**********************************************"
    print ""


def showStatus(zone):

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

    inner = (x2 - x1)**2 + (y2 - y1)**2
    return math.sqrt(inner)

def isOutofBounds()

