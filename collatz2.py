#This program evaluates the collatz sequenze for all positive intigers
#Return to this program at future data and add excpetion handling and counter

def collatz(number):
	if number % 2 == 0:
		number = number // 2
		print(number)
	else:
		number = 3 * number + 1
		print(number)
	return number
print("Please input a positive intiger greater than 1")
n = int(input())
while n!= 1:
	n = collatz(n)
	