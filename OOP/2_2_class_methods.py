__author__ = 'eric'
import math

class Dog(object):
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    def bark(self):
        print "Woof"

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printMe(self):
        print "({0},{1})".format(self.x, self.y)

    def move(self, x_inc, y_inc):
        """
        move the point by x_inc units and y_inc units
        """
        self.x = self.x + x_inc
        self.y = self.y + y_inc

    def get_distance(self, other_point):
        """
        Compute and return the distance between this point and other_point
        :param other_point: Point
        """
        return math.sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)




class Rectangle(object):
    """
    A class representing a rectangle
    """

    def __init__(self, width, height):
        """
        Initialize the rectangle
        :return: None
        """
        self.width = width
        self.height = height

    def get_area(self):
        """
        compute and return the area of the Rectangle
        :return: integer
        """
        return self.width * self.height




def example1():
    #create instance of a dog, call it's bark method
    sparky = Dog()
    sparky.bark()

def example2():
    # create an instance of a Point, set x,y values and call printMe()
    p1 = Point()
    p1.x = 12
    p1.y = 21

    p1.printMe()


def example3():
    """
    create an instance of a Rectangle, set attributes, output its area
    :return: None
    """
    rect = Rectangle()
    rect.width = 30
    rect.height = 50
    print rect.get_area()


def example4_1():
    p1 = Point()
    p1.x = 12
    p1.y = 21

    p1.printMe()

    #move the point
    p1.move(5,5)
    p1.printMe()

    p1.move(-20,0)
    p1.printMe()

def example4_2():

    """
    # commented out to get constructors to work

    p1 = Point()
    p1.x = 12
    p1.y = 21

    p2 = Point()
    p2.x = 100
    p2.y = 75

    print p1.get_distance(p2)
    """

example4_2()

def practice_2_2_1():
    """
    Modify the constructor of the Point class so that the x,y values are set at the time of instance creation.
    Write a program that creates an instance of a Point
    :return: None
    """

    #create an instance of a Point
    p1 = Point(2,3)
    p1.printMe()

    p1.move(10,10)
    p1.printMe()



def rectangle_construct_demo():

    square = Rectangle(20,20)
    print square.width
    print square.height

rectangle_construct_demo()