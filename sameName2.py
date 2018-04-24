#Short program to practice global variable
def spam():
	global eggs
	eggs = 'spam'
	
eggs = 'global'
spam()
print(eggs)
