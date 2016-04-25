__author__ = 'eric'


class Contact(object):
    """
    Class representing a single contact
    """
    def __init__(self, firstName, lastName, phone):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phone


class MyPhoneBook(object):
    """
    The "MyPhoneBook class
    """

    def __init__(self):
        self.numEntries = 0
        self.contacts = []  # a list to contain collection of Contact objects


    def add(self, firstName, lastName, phoneNumber):
        """
        Creates a new contact from parameter info and adds it to the list of contacts

        :param firstName: str
        :param lastName: str
        :param phoneNumber: str
        :return: None
        """

        self.contacts.append(Contact(firstName, lastName, phoneNumber))
        self.numEntries += 1

    def find(self, firstName, lastName):
        """
        Helper method to retrieve location (index) of a contact in the phonebook
        :param firstName: str
        :param lastName: str
        :return: int - index location of contact in list
        """

        for i in range(0, self.numEntries):
            if self.contacts[i].firstName == firstName and self.contacts[i].lastName == lastName:
                return i

        return -1 # not found

    def lookup(self, firstName, lastName):
        """
        Returns the phone number of the firstName and lastName
        :param firstName: str
        :param lastName: str
        :return: str
        """

        location = self.find(firstName, lastName)
        if location == -1:
            return ""
        else:
            return self.contacts[location].phoneNumber

    def getNumberEntries(self):
        return self.numEntries


class AddressContact(Contact):

    def __init__(self,firstName, lastName, phoneNumber, address):
        super(AddressContact,self).__init__(firstName, lastName, phoneNumber)
        self.address = address



class MyAddressBook(MyPhoneBook):

    """
    An object to model an address book
    """

    def __init__(self):
        """

        :return:
        """
        super(MyAddressBook, self).__init__()
        self.numEntries = 0
        self.addresses = []

    def addAddress(self, firstName, lastName, phoneNumber, address):
        """

        :param firstName: string
        :param lastName: string
        :param phoneNumber: string
        :param address: string
        :return: None
        """

        self.addresses.append(AddressContact(firstName, lastName, phoneNumber, address))


def demo_inheritance():
    # an example creation of an addressbook object
    book1 = MyAddressBook()
    book1.addAddress("William","Chan","555-555-5555","123 Main St, Toronto, On")
    print book1.addresses[0].firstName

class Animal(object):

    def __init__(self):
        print "Animal instantiated"

    def makeNoise(self):
        print "grr grr"


class Dog(Animal):

    def __init__(self):
        super(Dog, self).__init__()
        print "Dog instantiated"

    def fetch(self):
        print "Fetching the ball ..."

sparky = Dog()
sparky.fetch()