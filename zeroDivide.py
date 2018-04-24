# This program covers a simple example for error or exception handling
#Insert the code into a try block with an except and it run the full code
def spam(divideBy):
	try:
		return 42 / divideBy
	except ZeroDivisionError:
		print('Error: Invalid Argument.')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
# Placing the try and excpet will run the full code with in the fnc


#below the code will not run pass the 1 argument in spam

def spam(divideBy):
		return 42 / divideBy
try:
	print(spam(2))
	print(spam(12))
	print(spam(0))
	print(spam(1))
except ZeroDivisionError:
	print('Error: Invalid argument.')
	