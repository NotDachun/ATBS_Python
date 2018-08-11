l = ["When, in disgrace with fortune and men's eyes,\n", "I all alone beweep my \
outcast state,\n", "And trouble deaf heaven with my bootless cries,\n", "And \
look upon myself and curse my fate,"]

m, n = [], []
for num in range(len(l)):
	m.append(str(num))
	n.append(str(num * 2))
 	
for i, line in enumerate(l):
	l[i] = line.rstrip('\n')

total = [l, m, n]
filePaths = []
first = True

for path in total:
	for index in range(len(path)):
		if first:
			filePaths.append(list(path[]))
			print(filePaths)
		else:
			filePaths[index].append(path)
	first = not first


