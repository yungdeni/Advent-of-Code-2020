import re
file = open("input.txt", "r")
passmap = {}
lines = file.readlines()
count1 = 0
count2 = 0
data = ('byr', 'iyr','eyr','hgt','hcl','ecl','pid') #'cid'
byr = range(1920,2003)
iyr = range(2010, 2021)
eyr = range(2020,2031)
hgtcm = range(150,194)
hgtin = range(59,77)
hcl = re.compile('^#[a-f0-9]{6}$')
ecl = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
pid = re.compile('^[0-9]{9}$')

def checking():

	global count2
	part2check = 0
	if(int(passmap['byr']) in byr):

		part2check+= 1
	if(int(passmap['iyr']) in iyr):

		part2check+= 1
	if(int(passmap['eyr']) in eyr):

		part2check+= 1
	try:
		if('cm' in passmap['hgt']):
			check = passmap['hgt'].split('cm')
			if(int(check[0]) in hgtcm):
				part2check+= 1
	except:
		pass
	try:
		if('in' in passmap['hgt']):

			check = passmap['hgt'].split('in')

			if(int(check[0]) in hgtin):
				print(check[0])
				part2check+= 1
	except:
		pass
	if(passmap['ecl'] in ecl):

		part2check+= 1
	if (hcl.match(str(passmap['hcl']))):

		part2check+= 1				
	if (pid.match(str(passmap['pid']))):

		part2check+= 1
	if(part2check == 7):
		count2 +=1

for line in lines:
	#print(line.split(' '))
	keyv = line.split(" ")
	for k in keyv:
		i = k.split(":")

		if (i[0] != '\n'):
			passmap[i[0]] =  i[1].rstrip()
		else:
			if all(entry in passmap for entry in data):
				count1 += 1
				checking()
	
			passmap.clear()
#check after EOF
if all(entry in passmap for entry in data):
	count1 += 1
	checking()
	print(passmap)	
file.close()
print('Part 1: ' + str(count1))
print('Part 2: ' + str(count2))
