
file = open("input.txt", "r")
lines = file.read().split('\n')
file.close()
mem = {}
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"


get_bin = lambda x, n: format(x, 'b').zfill(n)



a = list(mask)
b = list(get_bin(11,36))

def masking(a,b):
    for idx, ch in enumerate(a):
        if a[idx] != 'X':
            b[idx] = a[idx]
    return int("".join(b),2)


print(masking(a,b))
for line in lines:
    line = line.split('=')
    if line[0].rstrip() == 'mask':
        mask = line[1].strip()
    elif 'mem' in line[0]:
        idx = line[0].split('[', 1)[1].split(']')[0]

        mem[idx] = masking(list(mask), list(get_bin(int(line[1].strip()), 36)))


sum = 0
for val in mem.values():
    sum += val

print(sum)