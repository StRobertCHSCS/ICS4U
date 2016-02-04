__author__ = 'eric'
import math

class Point():
    def __init__(self):
        self.x = 0
        self.y = 0

    def get_x(self):
        """
        Return the value x of the Point
        :return: int
        """
        return self.x

    def get_y(self):
        """
        Return the value y of the Point
        :return: int
        """

    def printMe(self):
        """
        Outputs the point in format (x,y)
        :return: None
        """

        print "({0},{1})".format(self.x,self.y)

    def move(self, x_inc, y_inc):
        """
        move the point by x_inc and y_inc amounts
        :param x_inc: value to increment x by
        :param y_inc: value to increment y by
        :return: None
        """
        self.x += x_inc
        self.y += y_inc

    def get_distance(self, p):
        """
        Compute the distance between self and point p
        :param p: Point
        :return: float, distance between self and point p
        """
        return math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)

point1 = Point()
point2 = Point()

point1.move(100,100)
point2.move(200,200)

print point1.get_distance(point2)



