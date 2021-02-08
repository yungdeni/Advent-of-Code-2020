import math
file = open("input.txt", "r")
lines = file.read().splitlines()

buses = []
index = 0
for bus in lines[1].split(","):
    if bus != "x":
        buses.append({'bus': int(bus), 'index': index})
    index += 1

# chinese remainder theorem from goooooooooooooooogle
def inv(a, m):
    m0 = m
    x0 = 0
    x1 = 1
    if (m == 1):
        return 0

    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
    if (x1 < 0):
        x1 = x1 + m0

    return x1

def findMinX(num, rem, k):
    prod = 1
    for i in range(0, k):
        prod = prod * num[i]

    result = 0

    for i in range(0, k):
        pp = prod // num[i]
        result = result + rem[i] * inv(pp, num[i]) * pp

    return result % prod


num = [(x['bus']) for x in buses]
rem = [-x['index'] for x in buses]
k = len(num)
print(num)
print(rem)
print("earliest timestamp is ", findMinX(num, rem, k))
