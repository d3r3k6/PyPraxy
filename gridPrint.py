#Design a program to print the grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#This is probably the way to do it based on what is presented so far

for a in range(len(grid[0])):
	for b in range(0, len(grid)):
		print(grid[b][a], end ='')
	print()	
	
print('.........')
		
		
#This is the elegant answer	using the zip function	
def fish():
    for line in zip(*grid):
        print(''.join(line))
fish()
		