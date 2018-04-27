# The task is to Write a function that takes a list value as an argument and return
#a string with all the items separated by a comma and a space, with and inserted before the last items

newList = ['apples', 'bananas', 'tofu', 'cats']

def convert(list):
	list = newList
	list[-1] = 'and ' + str(list[-1]) +'.'
	print(', ' .join(list))
	
convert(newList)