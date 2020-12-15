from itertools import combinations

file = open("input.txt", "r")
lines = file.read().split('\n')
file.close()
lines = [int(i) for i in lines]
lines.append(0)

lines.sort()
lines.append(lines[-1] + 3) 
onediff = 0
threediff = 0
part2 = 0
removed = []
for i in range(len(lines)-1):
    if lines[i+1] - lines[i] == 1:
        onediff+=1
    elif lines[i+1] - lines[i] == 3:
        threediff+=1
print(onediff * threediff)
combos = [0] * len(lines)
combos[0] = 1
for i in range(1, len(lines)):
    for j in range(i):
        if lines[i] - lines[j] <=3:
            combos[i] += combos[j]

print(combos[-1])