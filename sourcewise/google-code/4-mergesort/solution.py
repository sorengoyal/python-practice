def merge(a,b):
    c = []
    i,j = 0,0
    p,q = len(a), len(b)
    while len(c) != p+q:
        if i == p:
            c += b[j:]
            break
        elif j == q:
            c += a[i:]
            break
        elif a[i] <= b[i]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c

def mergesort(l):
    n = len(l)
    if n == 1:
        return l
    m = int(n / 2)
    a = mergesort(l[:m])
    b = mergesort(l[m:])
    return merge(a, b)

l = mergesort([6,5,4,3,2,1])
print(l)