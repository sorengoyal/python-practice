#http://practice.geeksforgeeks.org/problems/find-sum-of-different-corresponding-bits-for-all-pairs/0
from functools import reduce


T = int(input())
for i in range(0, T):
    n = int(input())
    raw = input()
    data = [int(x) for x in raw.split(' ') if x != '']
    onecount = [0]*32
    for num in data:
        invert = False
        if(num < 0):
            num = -num-1
            invert = True
        i = 0
        while num != 0:
            onecount[i] += (num&1) ^ invert
            num = num >> 1
            i = i + 1
    sum = 2*reduce(lambda sum, x: sum+x*(n-x), onecount, 0)
    print(sum%1000000007)