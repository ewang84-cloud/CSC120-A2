class Computer:

# All the attributes of the computer class, those that have been used in "procedural_resale_shop"
    description: str
    processor_type: str
    hard_drive_capacity: str
    memory: str
    operating_system: str
    price: float
    year_made: int
    OS: str
    
# constructor of the computer class
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price, OS):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        self.OS = OS

# Method of getting the name of the computer
    def getName(self):
        print (self.description)

# Method of getting the price of the computer
    def getPrice(self):
        print (self.price)

# Method of getting the processor type of the computer
    def getProcessorType(self):
        print (self.processor_type)
        
# Method of getting the Year the computer was made
    def getYearMade(self):
        print (self.year_made)

# Method of getting the Hard Drive Capacity of the computer
    def getHardDriveCapacity(self):
        print (self.hard_drive_capacity)

# Method of getting the memory of the computer
    def getMemory(self):
        print (self.memory)

# Method of getting the Operating System of the computer
    def getOperatingSystem(self):
        print (self.operating_system)

# Method of getting the OS of the computer
    def getOS(self):
        print (self.OS)

#  A method that can edit the Price of the computer to the input price
    def UpdatePrice(self, newPrice):
        self.price = newPrice

# A method that can edit the OS of the computer to the input OS
    def UpdateOS(self, newOS):
        self.OS = newOS


    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    # You'll remove this when you fill out your constructor


    # What methods will you need?