#Practice program to model an inventory printout for a video game
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

#This function print inventory
def dispalyInv(inventory):
    print("Your Current Inventory")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print(item_total + ' Items in inventory')
dispalyInv(stuff)

#Congats! You slayed a dragon. Below is his Inventory

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

#Function to add dragons inventory to yoru Inventory

def addToInv()
