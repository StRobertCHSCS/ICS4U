__author__ = 'eric'

class Student(object):

    def __init__(self, firstName, lastName, mark):
        self.firstName = firstName
        self.lastName = lastName
        self.mark = mark

class Classroom(object):

    def __init__(self,courseCode,rmNumber):
        self.courseCode = courseCode
        self.roomNumber = rmNumber

        self.students = []

    def __marks_sum(self):
        """
        Compute the sum of student marks
        return: float - the sum of student marks
        """

        total = 0
        for student in self.students:
            total = total + student.mark

        return total


    def getAverage(self):

        return float(self.__marks_sum())/len(self.students)


fabroa247 = Classroom('ICS4U',247)

fabroa247.students.append(Student('William','Chan',95))
fabroa247.students.append(Student('Kyle','Corpus',88))
fabroa247.students.append(Student('Grace','Li',100))
fabroa247.students.append(Student('Oliver','Wang',99))

print fabroa247.students[0].firstName
print fabroa247._Classroom__marks_sum()
print fabroa247.getAverage()

marino = Student("Marino","V",99)
marino.mark = 99.5
print marino.firstName



