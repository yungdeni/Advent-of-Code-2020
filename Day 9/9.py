file = open("input.txt", "r")
lines = file.read().split('\n')
file.close()
pointer = 0
count = 0
part1 = 0
preamble = {}
def check(preamble,line):
    global part1
    count = 0
    for k in preamble:
        count+=1
        target = (int(line) - int(k))
        if target <= 0:
            if count == 25:
                print(line)
                part1 = int(line)
            continue
        try:
            if preamble[str(target)] and (int(k) != target):
                return
        except:
            if count == 25:
                print(line)
                part1 = int(line)


for idx,line in enumerate(lines):
    if idx <=24:
        preamble[line] = True
        continue
    check(preamble,line)

    preamble.pop(lines[pointer])
    pointer+=1
    preamble[line] = True


for i in range(len(lines)):
    setc = 0
    for j in range(len(lines)):
        
        setc += int(lines[i+j])
        if(setc > part1):
            break
        if setc == part1 and j!= 0:
            #print(int(lines[i]) + int(lines[i+j]))
            lowest = part1
            highest = 0
            for k in range(i,i+j+1):
                if int(lines[k]) < lowest:
                    lowest = int(lines[k])
                if int(lines[k]) > highest:
                    highest = int(lines[k])
            print(highest + lowest)

