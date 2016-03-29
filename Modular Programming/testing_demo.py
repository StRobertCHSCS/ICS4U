__author__ = 'eric'

def my_squareroot(num):
    """
    compute the square root of num
    :param num:
    :return: float
    """

    return num**(0.5)

def wCount(astring):
    """
    Returns the number of 'w' characters in a given string
    :param astring: str - a string to count the w's
    :return: int
    """

    if astring == "":
        return 0
    else:
        if astring[0] == "w":
            return 1 + wCount(astring[1:])
        else:
            return wCount(astring[1:])

def midVal(alist):
    """
    Returns the middle value in a given list.  If there are an even numbers of items, return the value left of the middle
    :param alist: a list of values of any type
    :return - a value
    """

    mid = (len(alist) - 1)//2
    return alist[mid]


def isTriangle(a,b,c):
    """
    Given 3 angles, determine if they support a triangle shape
    :param a: int - an angle
    :param b: int - an angle
    :param c: int - an angle
    :return bool - True if it is a triangle
    """

    if a > 0 and b > 0 and c > 0 and (a+b+c == 180):
        return True
    else:
        return False


