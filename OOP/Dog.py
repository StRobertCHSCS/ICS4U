class Animal(object):

    def __init__(self):
        print "An Animal has been born"

    def eat(self):
        print "Munch Munch"

    def makeNoise(self):
        print "grr grr"


class Dog(Animal):

    def __init__(self):
        print "A dog has been born"

    def makeNoise(self):
        print "Ruff Ruff"

   
class Cow(Animal):

    def __init__(self):
        print "A cow has been born"

    def makeNoise(self):
        print "Moo Moo"

  

class Fox(Animal):
    def __init__ (self):
        print "a fox has been born"

    def makeNoise(self):
        print "Ding Ding Ding"

# -------------------
def main():
    sparky = Dog()
    sparky.makeNoise()
    sparky.eat()

    steve = Cow()
    steve.makeNoise()
    steve.eat()

    bruce = Fox()
    bruce.makeNoise()
    bruce.eat()


main()
