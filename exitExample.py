#This is a simple program to learn how to sys.exit()

import sys

while True:
	print('Type exit to quit')
	response = input()
	response = response.lower()
	if response == 'exit':
		sys.exit()
	print('You typed ' + response + '.')
	