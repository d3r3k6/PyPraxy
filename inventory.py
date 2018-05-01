#Practice program to model an inventory printout for a video game
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

#This function print inventory
def dispalyInv(inventory):
    print("Your Current Inventory")
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
dispalyInv(stuff)

print("Congats! You slayed a dragon. Below is his Inventory")

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print(dragonLoot)
#Function to add dragons inventory to yoru Inventory

def addToInv():
    for i in dragonLoot:
        stuff.setdefault("i", 0)
        stuff[i] = stuff[i] + 1
addToInv(dragonLoot)
print(stuff)
