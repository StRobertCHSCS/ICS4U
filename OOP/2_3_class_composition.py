__author__ = 'eric'

class Point(object):
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


class Student(object):

    def __init__(self, firstName, lastName, mark):
        """
        Initialize the student
        """
        self.firstName = firstName
        self.lastName = lastName
        self.mark = mark

class Classroom(object):

    def __init__(self, coursecode, roomNumber):
        self.coursecode = coursecode
        self.roomNumber = roomNumber
        self.students = []  #to contain Student objects


    def get_classAverage(self):
        """
        return the average mark of the students
        """

        total = 0

        #sum up the marks
        for student in self.students:
            total += student.mark

        return float(total)/len(self.students)


    def add_student(self, firstName, lastName, mark):

        self.students.append(Student(firstName, lastName, mark))



def example1_c():
    """
    Demonstrate the creation of a Rectangle object and set it's corner to a new point
    :return:None
    """

    tile = Rectangle(100,200)
    tile.set_corner(20,40)
    tile.show_corner()


def example2():
    """
    Create five Student objects.  Set their firstName, lastName and mark attributes.
    Create a Classroom object and append the student objects to the students attribute of the Classroom object
    print the class average of the classroom.

    :return: None
    """

    fab_students = [Student("Carlo", "Macha", 21)]
    fab_students.append(Student("Marino", "V", 99.4))
    fab_students.append(Student("Alena", "Calma", 13))
    fab_students.append(Student("Vince", "Mak", 100))
    fab_students.append(Student("Colin", "Wong", 96))

    # create a classroom
    fab_247 = Classroom("ICS4U", "247")

    # add students to the classroom
    for s in fab_students:
        fab_247.students.append(s)

    print fab_247.get_classAverage()

def example2_1():
    """
    uses the add_student method
    :return:
    """

    # create a classroom
    fab_247 = Classroom("ICS4U", "247")
    fab_247.add_student("Carlo", "Macha", 21)
    fab_247.add_student("Marino", "V", 99.4)
    fab_247.add_student("Alena", "Calma", 13)
    fab_247.add_student("Vince", "Mak", 100)
    fab_247.add_student("Colin", "Wong", 96)
