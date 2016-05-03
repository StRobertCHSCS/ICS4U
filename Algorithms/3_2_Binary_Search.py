__author__ = 'eric'

import random

def binary_search(key,myList):

    first = 0                       # initialize the first pointer to the beginning position
    last = len(myList)-1            # initialize the last pointer to the last position

    while first <= last:            # repeat while first and last pointer have not crossed
        mid = (first + last)//2     # compute the location of the middle value
        midItem = myList[mid]       # get the value at the middle position

        if key > midItem:           # check if key is greater than mid value
            first = mid + 1         # adjust the first pointer, search the upper half

        elif key < midItem:         # check if key is lower than mid value
            last = mid-1            # adjust the last pointer, search the lower half

        else:
            return mid              # key found, return position of the key

    return - 1                      # key not found


def example1():
    bday_list = random.sample(range(1,365),25)
    bday_list.sort()

    for i in range(5):
        user_num = input("Enter a number: ")
        location = binary_search(user_num, bday_list)
        if location > -1:
            print "number found at location", location
        else:
            print "number not in list"



def insert_linear():

    number = 0
    int_list = []

    while number != -1:
        # get the number from user input
        number = input("Enter a number (-1 to stop):  ")

        if number != -1:

            #add number to the list
            if len(int_list) > 0:
                # use linear search and iterate through list to find insert location



                int_list.insert(location, number)

            else:
                int_list.append(number)

            print int_list
