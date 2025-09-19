class Computer:
    name: str
    price: float
    OS: str

    def __init__(self, name, price, OS):
        self.name = name
        self.price = price
        self.OS = OS

    def getName(self):
        print (self.name)

    def getPrice(self):
        print (self.price)

    def getOS(self):
        print (self.OS)

    def UpdatePrice(self, newPrice):
        self.price = newPrice

    def UpdateOS(self, newOS):
        self.OS = newOS


    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    # You'll remove this when you fill out your constructor


    # What methods will you need?