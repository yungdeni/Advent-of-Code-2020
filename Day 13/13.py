from functools import reduce
file = open("input.txt", "r")
lines = file.read().split('\n')
file.close()

timestamp = lines[0]
buses = lines[1].split(",")

excl = ["x"]
earliest = []
for bus in [x for x in buses if x not in excl]:
    early = 0
    while early < int(timestamp):
        early+= int(bus)
    earliest.append((early, int(bus)))
    #print(bus)
print(timestamp)
print((min(earliest)[0] - int(timestamp)) * min(earliest)[1])


n = []
a = []

def chinese_remainder(n, a):
    prod = 1
    for i in range(0, len(n)):
        prod = prod * n[i]

    result = 0

    for i in range(0, len(n)):
        pp = prod // n[i]
        result = result + a[i] * mul_inv(pp, n[i]) * pp

    return result % prod

def mul_inv(a, b):
    m0 = b 
    y = 0
    x = 1
  
    if (b == 1): 
        return 0
  
    while (a > 1): 
  
        q = a // b 
  
        t = b 
        b = a % b 
        a = t 
        t = y 
        y = x - q * y 
        x = t 

    if (x < 0): 
        x = x + m0 
  
    return x 


for idx, bus in enumerate(buses):
    if bus != 'x':
        n.append(int(bus))
        a.append(idx)


a = [-x for x in a]

print(n)
print(a)
print(chinese_remainder(n,a))
