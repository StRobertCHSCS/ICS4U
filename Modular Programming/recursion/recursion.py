__author__ = 'eric'
def countdown(n):
    """
    recursive function to countdown from n to 1 then Blastoff!
    :param n: int - starting number to countdown from
    :return: None
    """
    if n <= 0:
        print 'Blastoff!'
    else:
        print n
        countdown(n-1)


def printn(mystring,n): #definition
    """
    Outputs a string n times
    :param mystring: str - the string to print
    :param n: int - number of times to output mystring
    :return: None
    """
    # kick check
    if n <= 0:
        return None #kick

    # action
    else:
        print mystring # action
        # inception step (leave one behind)
        printn(mystring,n-1)


def sumN_iter(n):
    """
    Computes the num of numbers from 1 to n.  An iterative (loop) solution.
    :param n: int
    :return: int - sum of numbers from 1 to n.
    """

    total = 0
    for i in range(n + 1):
        total = total + i
    return total


def sumN_rec(n):
    """
    Computes the num of numbers from 1 to n.  A recursive solution.
    :param n: int
    :return: int - sum of numbers from 1 to n.
    """
    if n == 1:
        return 1
    else:
        return n + sumN_rec(n - 1)


def rpow_iter(x,y):
    """
    Compute x to the power of y (x**y).  An iterative solution (loops)
    :param x: int - the base
    :param y: int - the exponent
    :return: x**y
    """
    pow = x
    for i in range(y-1):
        pow = pow * x
    return pow


def rpow_recur(x, y):
    """
    Compute x to the power of y (x**y).  An recursive solution
    :param x: int - the base
    :param y: int - the exponent
    :return: x**y
    """
    if y == 0:
        return 1
    else:
        return x * rpow_recur(x,y-1)


def factorial(n):
    """
    Compute the factorial of n
    :param n: int > 0
    :return: int -  n!
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def recur_len(str):
    """
    Compute the length of a str
    :param str: str
    :return: int
    """

    if str == '':
        return 0
    else:
        return 1 + recur_len(str[1:])

def recursive_reverse(mystring):

    if mystring == "":
        return mystring
    else:
        return recursive_reverse(mystring[1:]) + mystring[0]

def isPalindrome(mystring):
    if mystring == "":
        return True
    elif len(mystring) == 1:
        return True
    else:
        return mystring[0] == mystring[-1] and isPalindrome(mystring[1:-1])


def rec_min(numlist):

    if len(numlist) == 1:
        return numlist[0]
    else:
        min_of_the_rest = rec_min(numlist[1:])
        if numlist[0] <= min_of_the_rest:
            return numlist[0]
        else:
            return min_of_the_rest

print rec_min([4,6,2,1,8,9])





