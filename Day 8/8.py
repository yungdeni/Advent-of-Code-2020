file = open("input.txt", "r")
lines = file.readlines()
file.close()
acc = 0
pcr = 0
pcrlist = []
linesOG = lines[:]
print(lines[0].split(" ")[0])

while True:
    instr = lines[pcr].split(" ")[0]

    if pcr in pcrlist:
        break
    pcrlist.append(pcr)
    if instr == 'nop':
        pcr += 1
    elif instr == 'acc':
        acc += int(lines[pcr].split(" ")[1])
        pcr += 1
    elif instr == 'jmp':
        pcr += int(lines[pcr].split(" ")[1])

print("Part 1: " + str(acc))


def findNextJmpNop(chlist):
    counter = 0
    for line in linesOG:

        instr = line.split(" ")[0]
        if instr == 'jmp' or instr == 'nop':
            if counter in chlist:
                counter += 1
                continue
            else:
                return counter
    
        counter += 1
    return counter
acc = 0
pcr = 0
pcrmax = 0
pcrlist = []
changelist = []
while True:
    
    #print(len(lines))
    if pcr in pcrlist:
        
        acc = 0
        pcr = 0
        pcrlist = []
        lines = linesOG[:]
        index = findNextJmpNop(changelist)
        changelist.append(index)
        try:
            toswitch = lines[index].split(" ")[0]
            param = lines[index].split(" ")[1]
            if toswitch == 'jmp':
                toswitch = 'nop'
            else:
                toswitch = 'jmp'
            lines[index] = toswitch + " " + param
        except:
            continue
    pcrlist.append(pcr)
    try:
        instr = lines[pcr].split(" ")[0]
    except:
        break
        
    if pcr < len(lines) + 1:
        if instr == 'nop':
            pcr += 1
        elif instr == 'acc':
            acc += int(lines[pcr].split(" ")[1])
            pcr += 1
        elif instr == 'jmp':
            pcr += int(lines[pcr].split(" ")[1])
    else:
        break
    
print("Part 2: " + str(acc))