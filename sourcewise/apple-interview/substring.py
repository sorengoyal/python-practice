from functools import reduce
import sys

def indexOf(primary, secondary):
    p = 0
    s = 0
    while p < len(primary):
        if s == len(secondary):
            return p - s
        if primary[p] == secondary[s]:
            p = p + 1
            s = s + 1
        else:
            p = p + 1
            s = 0
        if s == len(secondary):
            return p - s
    return -1


def replace(primary, secondary, index):
    p = list(primary)
    for i in range(len(secondary)):
        p[index+i] = secondary[i]
    return reduce(lambda acc,ch: acc + ch, p)

p = input()
s = input()
r = input()
index = indexOf(p, s)
if index == -1:
    print("Not found: " + s)
    sys.exit()
print(replace(p, r, index))