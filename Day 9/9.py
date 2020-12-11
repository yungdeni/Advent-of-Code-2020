file = open("input.txt", "r")
lines = file.read().split('\n')
file.close()
pointer = 0
count = 0

preamble = {}
def check(preamble,line):
    count = 0
    for k in preamble:
        count+=1
        target = (int(line) - int(k))
        if target <= 0:
            if count == 25:
                print(line)
            continue
        try:
            if preamble[str(target)] and (int(k) != target):
                return
        except:
            if count == 25:
                print(line)




for idx,line in enumerate(lines):
    if idx <=24:
        preamble[line] = True
        continue
    check(preamble,line)

    preamble.pop(lines[pointer])
    pointer+=1
    preamble[line] = True


