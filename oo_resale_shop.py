from computer import Computer

class ResaleShop:

# The attributes of the Resale Shop, with an empty list of computers that serves as the inventory 
    name: str
    inventory: list[Computer] = []

# Constructor of the Resale Shop
    def __init__(self, name: str):
        self.name = name
        self.inventory = []

# Buying a computer, adding the computer into the inventory
    def BuyComputer(self, computer: Computer):
        self.inventory.append(computer)

# Selling a computer is there is, and delete it from the inventory; if there's non of this computer in stock, don't add or minus anything from the inventory
    def SellComputer(self, computer: Computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
            print("Successfully sold", computer.name)
        else:
            print("Computer not in stock")

# Print out all the computers in the inventory
    def PrintInventory(self):
        i=0
        for computer in self.inventory:
            print(i,".", computer.name, ",", computer.price, ",", computer.OS)
            i+=1
        else:
            if i==0:
                print("No computers")

# Print the number of computer in the inventory
    def PrintNumberOfComputers(self):
        print("Number of computers:", len(self.inventory))
    
# Checking if it works in the Main
def main():
    myComputer = Computer("Mac Air", 1000, "macOS")
    myShop = ResaleShop("My Shop")
    myShop.SellComputer(myComputer)
    myShop.BuyComputer(myComputer)
    myShop.SellComputer(myComputer)
    myShop.PrintInventory()


    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    # You'll remove this when you fill out your constructor

    # What methods will you need?