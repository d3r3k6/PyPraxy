#This program ask for a name and correct password

while True:
	print('Who are you?')
	name = input()
	if name != 'Derek':
		continue
	print('Hello, Derek. What is the password?')
	password = input ()
	if password == 'swordfish':
		break
print('Access Granted.')			
