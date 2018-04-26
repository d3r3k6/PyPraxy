#Short prorgam to understand how arguments get passed to functions

def eggs(someParameter):
	someParameter.append('Hello')
spam = [1, 2, 3]
print(spam)
print('call eggs fnc')
eggs(spam)
print(spam)	