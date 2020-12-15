from itertools import cycle, islice
file = open("input.txt", "r")
lines = file.read().split('\n')
file.close()


def numsplit(s):
    head = s.rstrip('0123456789')
    tail = s[len(head):]
    return head, tail

lines = [numsplit(s) for s in lines]
directions = {'N' : 0, 'S' : 0, 'E' : 0, 'W' : 0}
pointer = 'E'
cycdirs = ['N','E','S','W']

def changePointer(rot, deg):
    global pointer
    global cycdirs
    if rot == 'R':
        start = cycdirs.index(pointer)
        for i in range(deg//90):
            start = (start + 1) % len(cycdirs)
            pointer = cycdirs[start]
            
    elif rot == 'L':
        start = cycdirs.index(pointer)
        for i in range(deg//90):
            start = (start - 1) % len(cycdirs)
            pointer = cycdirs[start]
    else:
        return

def shiftDict(dic, n):
    return dict(zip(dic, islice(cycle(dic.values()), n, None)))

for line in lines:
    if line[0] == 'R':
        changePointer('R',int(line[1]))
    elif line[0] == 'L':
        changePointer('L',int(line[1]))
    elif line[0] == 'N':
        directions[line[0]] += int(line[1])
    elif line[0] == 'S':
        directions[line[0]] += int(line[1])
    elif line[0] == 'E':
        directions[line[0]] += int(line[1])
    elif line[0] == 'W':
        directions[line[0]] += int(line[1])
    elif line[0] == 'F':
        directions[pointer] += int(line[1])


print(abs(directions['N'] - directions['S']) +abs(directions['W'] - directions['E']))

directions = {'N' : 0, 'E' : 0, 'S' : 0, 'W' : 0}
waypoint = {'N' : 1, 'E' : 10, 'S' : 0, 'W' : 0}

for line in lines:
    if line[0] == 'R':
        waypoint = shiftDict(waypoint, 3 * int(line[1])//90)
    elif line[0] == 'L':
        waypoint = shiftDict(waypoint, 1 * int(line[1])//90)
    elif line[0] == 'N':
        waypoint[line[0]] += int(line[1])
    elif line[0] == 'S':
        waypoint[line[0]] += int(line[1])
    elif line[0] == 'E':
        waypoint[line[0]] += int(line[1])
    elif line[0] == 'W':
        waypoint[line[0]] += int(line[1])
    elif line[0] == 'F':
        for key in directions.keys():
            directions[key] += waypoint[key] * int(line[1])

print(abs(directions['N'] - directions['S']) +abs(directions['W'] - directions['E']))
    #print(waypoint)