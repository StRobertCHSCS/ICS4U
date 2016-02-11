__author__ = 'eric'
import math

def distance(x1, y1, x2, y2):
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return d

def main():
    x_1 =input("Enter an x-value for the first point: ")
    y_1 =input("Enter an y-value for the first point: ")

    x_2 = input("Enter an x-value for the second point: ")
    y_2 = input("Enter an y-value for the second point: ")

    dist = distance(x_1, y_1, x_2, y_2)
    print "The distance between the points is", dist

main()
