from itertools import islice
file = open("input.txt", "r")
inputList = file.read().splitlines()
file.close()

stepr1d1 = 0
stepr3d1 = 0
stepr5d1 = 0
stepr7d1 = 0
stepr1d2 = 0
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0

for i in islice(inputList,1,None):
	stepr1d1 = (stepr1d1 + 1) % len(i)
	stepr3d1 = (stepr3d1 + 3) % len(i)
	stepr5d1 = (stepr5d1 + 5) % len(i)
	stepr7d1 = (stepr7d1 + 7) % len(i)
	if(i[stepr7d1] == '#'):
		total4 += 1	
	if(i[stepr5d1] == '#'):
		total3 += 1
	if(i[stepr3d1] == '#'):
		total2 += 1
	if(i[stepr1d1] == '#'):
		total1 += 1
		
for i in islice(inputList,2,None,2):
		stepr1d2 = (stepr1d2 + 1) % len(i)
		if(i[stepr1d2] == '#'):
			total5 += 1
print("Part 1: " + str(total2))
print("Part 2: " + str(total1 * total2 * total3 * total4 * total5))