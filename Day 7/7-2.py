file = open("input.txt", "r")
lines = file.readlines()
file.close()
bagDict = {}
excl = ["bag", "bags", "contain", "contains", ",", "bag.", "bags.", "bags,", "bag,", "bag.\n", "bags.\n"]
for line in lines:
    line = line.split(' ')
    line = [i for i in line if not i in excl]

    for j in range(2,len(line),3):
        temp = [" ".join(line[j:j+3])]
        try:
            bagDict[(" ".join(line[0:2]))] += temp
        except:
            bagDict[(" ".join(line[0:2]))] = temp

alreadytraversed = []
def reccheck(k):
    test = 1
    global alreadytraversed
    try:
        for i in bagDict[k]:
            #print(i)
            if i not in alreadytraversed:
                i = i.split()

                alreadytraversed.append(i[1] + " " + i[2])
                test += reccheck(i[1] + " " + i[2]) * int(i[0])
        return test
    except:
        return 1
print(bagDict)
print(reccheck('shiny gold') - 1)