#This is a program that explores the Collatz Sequence
#This is an algorithm that wil evaluate all positive integers down to 1 as far as we know

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

n = input("Enter a positive integer: ")
while n != 1:
    n = collatz(int(n))
		

			
	
	
	
	




		
	

