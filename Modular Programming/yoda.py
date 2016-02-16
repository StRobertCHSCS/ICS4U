__author__ = 'eric'

"""
Implentation of the YODA problem on dmoj.ca
https://dmoj.ca/problem/coci15c4p1
"""

def processDigit(int_digit1, int_digit2):
    """
    Process two integers based on collision rules stated in problem:

    'During collision, each digit of one number compares itself to the corresponding digit
    of the other number (the least significant digit with the other’s least significant digit,
    and so on). The smaller digit “falls out” of the number containing it.
    Additionally, if the digits are the same, nothing happens.'

    :param int_digit1: int - first int to compare
    :param int_digit2: int - second int to compare
    :return: int/"", int/"" - resulting int or empty string based on collision rules
    """

    if int_digit1 > int_digit2:
        return str(int_digit1), ""

    elif int_digit1 < int_digit2:
        return "", str(int_digit2)

    else:
        return str(int_digit1), str(int_digit2)

    return out_str1, out_str2


def convert_yoda(numstr):
    if numstr == "":
        return 'YODA'
    else:
        return int(numstr)


def yoda(int1,int2):
    """

    :param int1: int - first number input
    :param int2: int - second number input
    :return: int, int - the resulting integers after collision
    """

    final1 = ""
    final2 = ""
    str_int1 = str(int1)
    str_int2 = str(int2)

    i = len(str_int1) - 1 # pointer for first integer
    j = len(str_int2) - 1 # pointer for second integer

    while i >= 0 and j >= 0:
        # compare digits and keep or drop
        collide_digit1, collide_digit2 = processDigit(str_int1[i], str_int2[j])


        # add appropriate digit to the resulting strings
        final1 = collide_digit1 + final1
        final2 = collide_digit2 + final2

        i -= 1
        j -= 1

    if j >= 0:
        # the second int is longer, add the rest of the digits
        while j >=0:
            final2 = str_int2[i] + final2
            j -= 1

    elif i >= 0:
        # the first int is longer, add the rest of the digits
        while i >= 0:
            final1 = str_int1[i] + final1
            i -=1

    # convert to yoda or int
    final1 = convert_yoda(final1)
    final2 = convert_yoda(final2)

    return final1, final2


def main():
    """
    A main program to test sample input
    :return: None
    """

    print yoda(300,500)
    print yoda(65743, 9651)
    print yoda(2341, 6785)

main()










