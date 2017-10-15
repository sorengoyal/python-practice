from math import sqrt
primes = ['x']*10000
pairData = {
            4: (2, 2),
            6: (3, 3)
            }


def isPrime(x):
    if primes[x] == 'x':
        result = True
        for y in range(2, int(sqrt(x))):
            if x%y == 0:
                result = False
                break
        primes[x] = result
    return primes[x]


def findPair(n):
    for m in range(4, n+2, 2):
        if m in pairData:
            continue
        d = 2
        (a, b) = pairData[m - d]
        found = False
        while not found:
            if isPrime(a + d):
                pairData[m] = (a + d, b)
                found = True
            elif isPrime(b + d):
                pairData[m] = (a, b + d)
                found = True
            else:
                d += 2
                (a, b) = pairData[m - d]
    return pairData[n]
T = int(input())
for i in range(0, T):
    N = int(input())
    print('%d %d' % findPair(N))
