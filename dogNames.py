#Program to practice adding items to a list

dogNames = []
while True:
	print('Enter the name of dog ' + str(len(dogNames) + 1) + ' or enter nothing to stop.')
	name = input()
	if name == '':
		break
	dogNames = dogNames + [name] #list concatenation
print("The dog's names are:")
for name in dogNames:
	print(' ' + name)
	
dogNames.clear() #Clears the list to add new items next time
print(len(dogNames))	#Check to see if list clear, just because
