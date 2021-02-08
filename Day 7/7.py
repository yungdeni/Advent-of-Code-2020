import re
file = open("input.txt", "r")
lines = file.readlines()
file.close()
bagDict = {}
excl = ["bag", "bags", "contain", "contains", ",", "bag.", "bags.", "bags,", "bag,", "bag.\n", "bags.\n"]
part1 = 0
for line in lines:
	line = re.sub(r'\d+','',line)

	line = line.split()
	print(line)
	line = [i for i in line if not i in excl]
	
	for j in range(2,len(line),2):
		try:
			bagDict[(" ".join(line[j:j+2]))] += [" ".join(line[0:2])]
		except:
			bagDict[(" ".join(line[j:j+2]))] = [" ".join(line[0:2])]
alreadytraversed = []
def reccheck(k):
	test = 0
	global alreadytraversed
	try:	
		for i in bagDict[k]:
			if i not in alreadytraversed:
				alreadytraversed.append(i)
				print(i)
				reccheck(i)
		return
	except:
		return 
print(reccheck('shiny gold'))
print(len(alreadytraversed))
