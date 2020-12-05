import math
file = open("input.txt", "r")
lines = file.readlines()
file.close()
rows = [*range(0,128)]
columns = [*range(0,8)]
highestseatid = 0
seatidlist = []

def rowcheck(lis,rowchars):
	length = math.floor(len(lis)/2)
	if (length == 0):
		length =1
	check = [lis[i:i + length] for i in range(0, len(lis), length)]
	if(rowchars == ""):
		return check

	if(rowchars[0] == 'F'):
		check = check[0]
	elif (rowchars[0] == 'B'):
		check = check[1]
	return rowcheck(check, rowchars[1:])

def colcheck(lis,colchars):
	length = math.floor(len(lis)/2)
	if (length == 0):
		length = 1
	check = [lis[i:i + length] for i in range(0, len(lis), length)]
	if(colchars == ""):
		return check
	if(colchars[0] == 'L'):
		check = check[0]
	elif(colchars[0] == 'R'):
		check = check[1]
	return colcheck(check, colchars[1:])	

for line in lines:
	if(line != '/n' or line != ""):
		line = line.rstrip()
		r = rowcheck(rows,line[:7])[0][0]
		c = colcheck(columns,line[-3:])[0][0]
		seatidlist.append((r * 8) + c)
seatidlist.sort()
highestseatid = seatidlist[-1]

missing = [x for x in range(seatidlist[0], seatidlist[-1]+1)if x not in seatidlist]
print("Part: " + str(highestseatid))
print("Part 2: " + str(missing[0]))

