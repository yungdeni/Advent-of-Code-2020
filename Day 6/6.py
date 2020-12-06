file = open("input.txt", "r")
lines = file.readlines()
file.close()
q = ""
q2 = []

part1 = 0
part2 = 0
for line in lines:
	if(line != '\n'):
		q += line.rstrip()
		q2.append(line.rstrip())
	else: 
		part1 += (len(set(q)))
		print(q2)
		try:
			check = q2[0]
		except:
			check = ""
		for char in check:
			if all(char in item for item in q2):
				part2 += 1
		q = ""
		q2 = []

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))