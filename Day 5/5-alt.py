import math
file = open("input.txt", "r")
lines = file.readlines()
file.close()
seatidlist = []
for line in lines:
	binNum = ""
	for char in line:
		if char == "B":
			binNum += '1'
		elif char == "F":
			binNum += '0'
		elif char == "R":
			binNum += '1'
		elif char == 'L':
			binNum +='0'
	seatidlist.append(int(binNum, 2))
seatidlist.sort()
missing = [x for x in range(seatidlist[0], seatidlist[-1]+1)if x not in seatidlist]
print('Part1: ' + str(seatidlist[-1]))
print('Part 2: ' + str(missing[0]))