tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidth = 0
for row in tableData:
	for element in row:
		if len(element) > colWidth:
			colWidth = len(element)

for colIn in range(len(tableData[0])):
	for rowIn in range(len(tableData)):
		print(tableData[rowIn][colIn].rjust(colWidth), end='')
	print()

	primt()