from computer import Computer

class ResaleShop:
    name: str
    inventory: list[Computer] = []

    def __init__(self, name: str):
        self.name = name
        self.inventory = []

    def BuyComputer(self, computer: Computer):
        self.inventory.append(computer)

    def SellComputer(self, computer: Computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
            print("Successfully sold", computer.name)
        else:
            print("Computer not in stock")

    def PrintInventory(self):
        i=0
        for computer in self.inventory:
            print(i,".", computer.name, ",", computer.price, ",", computer.OS)
            i+=1
        else:
            if i==0:
                print("No computers")

    def PrintNumberOfComputers(self):
        print("Number of computers:", len(self.inventory))
    

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