class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"


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
        Sets the corner to a new point at x, y
        :param x: int - new x value for the corner
        :param y: int - new y value for the corner
        :return: None
        """
        self.corner = Point(x,y)

class Box(Rectangle):
    """
    A Box object
    """

    def __init__(self, length):

        self.width = length
        self.height = length
        self.corner = Point(0,0)
        "Box instantiated"


    def get_side(self):
        return self.width

    def __str__(self):
        return "Box - {length: {0}, at {1}".format(self.get_side(), self.corner.__str__())

giftbox = Box(10)
print giftbox.get_side()
print giftbox
