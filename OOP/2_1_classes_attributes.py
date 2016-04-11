from math import sqrt

class Point(object):
    """
    A class representing a coordinate point
    """
    def __init__(self):
        """
        Initialize x,y values to 0
        :return: None
        """
        self.x = 0
        self.y = 0

class Rectangle(object):
    """
    A object that models a rectangle
    Practice #1 in the notes
    """

    def __init__(self):
        """
        Initialize the rectangle with default width and height
        :return: None
        """

        self.width = 0
        self.height = 0

class Address(object):
    """
    Models an Address object with attributes for a street address
    """

    def __init__(self):
        self.address_line1 = ""
        self.address_line2 = ""
        self.postal_code = ""
        self.province = ""
        self.city = ""
        self.country = "Canada"


def point_demo():
    # create an instance of a Point
    point1 = Point()

    # This does NOT set the x values of the point
    x = 2

    # This also does NOT set the x values of the point
    Point.x = 2

    # correctly set the x and y values of the point1 instance
    point1.x = 2
    point1.y = 3

    print point1.x, point1.y

def point_distance():
    """
    Create two point object and return the distance between the points
    :return: float
    """


    #create point1 and point2 instances
    point1 = Point()
    point2 = Point()

    # assign values to point objects
    point1.x = 15
    point1.y = 15

    point2.x = 5
    point2.y = 5

    #compute distance
    distance = sqrt((point2.y - point1.y)**2 + (point2.x - point1.x)**2)
    return distance

def rect_area(width, height):

    # create an instance of a rectangle
    tile = Rectangle()
    tile.width = width
    tile.height = height

    # compute and return rectangle area
    return tile.width * tile.height


def print_address(addr):

    addr_str = addr.address_line1
    if addr.address_line2 != "":
        addr_str += "\n" + addr.address_line2
    addr_str += "\n" + addr.city
    addr_str += "\n" + addr.postal_code
    addr_str += "\n" + addr.province
    addr_str += "\n" + addr.country

    print addr_str

def address_demo():

    # create one address object - work
    work = Address()
    work.address_line1 = "123 Main St."
    work.address_line2 = "Unit 2B"
    work.postal_code = "L3T 7P1"
    work.city = "Thornhill"
    work.province = "Ontario"

    # create a home address object
    home = Address()
    home.address_line1 = "578 Bayview Ave."
    home.postal_code = "L4G 7T4"
    home.city = "Aurora"
    home.province = "Ontario"

    print_address(home)
    print ""
    print_address(work)

address_demo()


