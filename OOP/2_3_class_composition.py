__author__ = 'eric'

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printMe(self):
        print "("+str(self.x)+", "+str(self.y)+")"


class Rectangle(object):
    """
    A class representing a rectangle
    """

    def __init__(self, w, h):
        """
        Initialize the rectangle
        :return: None
        """

        self.width = w
        self.height = h
        self.corner = Point(0,0)


    def set_corner(self, x, y):
        """
        set the location of the rectangle
        :param x: int
        :param y: int
        :return: None
        """

        self.corner.x = x
        self.corner.y = y

    def show_corner(self):
        """
        output the location of the rectangle
        :return: None
        """

        self.corner.printMe()


def example1_c():
    """
    Demonstrate the creation of a Rectangle object and set it's corner to a new point
    :return:None
    """

    tile = Rectangle(100,200)
    tile.set_corner(20,40)
    tile.show_corner()

example1_c()