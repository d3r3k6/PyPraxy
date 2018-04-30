#This program counts the number of occurences of each letter in a string
#Will also import pretty print to ensure output is more readable

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
	count.setdefault(character, 0)
	count[character] = count[character]+1

pprint.pprint(count)