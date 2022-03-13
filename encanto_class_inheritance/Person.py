class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class FamilyMadrigal(Person):
    def __init__(self, fname, gift="I don't have a gift."):
        super().__init__(fname, "Madrigal")
        self.gift = gift

    def printgift(self):
        print(self.gift)

    def setgift(self, newgift):
        self.gift = newgift

    def introduce(self):
        print(f'Hi my name is {self.firstname} {self.lastname}, and {self.gift}')

