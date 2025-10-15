class Computer:
    description: str
    processor_type: str
    hard_drive_capacity: str
    memory: str
    operating_system: str
    price: float
    year_made: int
    OS: str
    

    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price, OS):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        self.OS = OS


    def getName(self):
        print (self.description)

    def getPrice(self):
        print (self.price)

    def getProcessorType(self):
        print (self.processor_type)

    def getYearMade(self):
        print (self.year_made)

    def getHardDriveCapacity(self):
        print (self.hard_drive_capacity)

    def getMemory(self):
        print (self.memory)

    def getOperatingSystem(self):
        print (self.operating_system)

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