file = open("input.txt", "r")
lines = file.read().split('\n')
file.close()

nextline = ""
nextround = []
lines.append(len(lines[0])  * '.')
lines.insert(0,len(lines[0]) * '.')
for idx, line in enumerate(lines):
    lines[idx] = "." + line + "."

def adjecent(i,j,seat):
    neighbours = ""
    neighbours += prevround[i-1][j]
    neighbours += prevround[i][j-1]
    neighbours += prevround[i-1][j-1]
    neighbours += prevround[i+1][j]
    neighbours += prevround[i][j+1]
    neighbours += prevround[i+1][j+1]
    neighbours += prevround[i+1][j-1]
    neighbours += prevround[i-1][j+1]

    if seat == '#':
        if neighbours.count("#") >= 4:
            return "L"
        else:
            return '#'
    if seat == 'L':
        if neighbours.count("#") == 0:
            return "#"
        else:
            return 'L'
def findfirstsight(di,dj,i,j):
    x = 1
    while True:
        if (i + (di*x)) < 1 or j + (dj *x) < 1 or j + (dj *x) >= len(prevround[0]) or i + (di*x) >= len(prevround):
            return " "
        elif prevround[i + (di*x)][j + (dj *x)] == "#":
            return "#"
        elif prevround[i + (di*x)][j + (dj *x)] == "L":
            return  "L"
        x += 1

def lineofsight(i,j,seat):
    neighbours = ""
    found = 0
    x = 0
    neighbours += findfirstsight(-1,0,i,j)
    neighbours += findfirstsight(0,-1,i,j)
    neighbours += findfirstsight(-1,-1,i,j)
    neighbours += findfirstsight(1,0,i,j)
    neighbours += findfirstsight(0,1,i,j)
    neighbours += findfirstsight(1,1,i,j)
    neighbours += findfirstsight(1,-1,i,j)
    neighbours += findfirstsight(-1,1,i,j)

    if seat == '#':
        if neighbours.count("#") >= 5:
            return "L"
        else:
            return '#'
    if seat == 'L':
        if neighbours.count("#") == 0:
            return "#"
        else:
            return 'L'

prevround = lines

while True:
    for i in range(0,len(prevround)):
        for j in range(0,len(prevround[0])):   
            if prevround[i][j] == '.':
                nextline += "."
            else:
                nextline += adjecent(i,j,prevround[i][j])
        nextround.append(nextline)
        nextline = ""

    if prevround == nextround:
        break
    else:
        prevround = nextround[:]
        nextround = []

part1 = 0
for line in prevround:
    for seat in line:
        if seat == "#":
            part1+= 1

part2 = 0
print(part1)
prevround = lines
nextround = []
while True:
    for i in range(0,len(prevround)):
        for j in range(0,len(prevround[0])):   
            if prevround[i][j] == '.':
                nextline += "."
            else:
                nextline += lineofsight(i,j,prevround[i][j])
        nextround.append(nextline)
        nextline = ""

    if prevround == nextround:
        break
    else:
        prevround = nextround[:]

        nextround = []

for line in prevround:
    for seat in line:
        if seat == "#":
            part2+= 1

print(part2)