__author__ = 'eric'
def countdown(n):
    if n <= 0:
        print 'Blastoff!'
    else:
        print n
        countdown(n-1)


def printn(mystring,n): #definition
    # kick check
    if n <= 0:
        return None #kick

    # action
    else:
        print mystring # action
        # inception step (leave one behind)
        printn(mystring,n-1)

def sumN_iter(n):
    total = 0
    for i in range(n + 1):
        total = total + i
    return total


def sumN_rec(n):
    if n == 1:
        return 1
    else:
        return n + sumN_rec(n - 1)

def rpow_iter(x,y):
    pow = x
    for i in range(y-1):
        pow = pow * x
    return pow

print rpow_iter(2,3)
