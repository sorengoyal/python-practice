def rotateMatrix(m):
    i = 1
    R = len(m)+1
    while i <= R/2:
        for j in range(i,R-i):
                temp = m[i-1][j-1]
                m[i-1][j-1] = m[j-1][R-i-1]
                m[j-1][R-i-1] = m[R-i-1][R-j-1]
                m[R-i-1][R-j-1] = m[R-j-1][i-1]
                m[R-j-1][i-1] = temp
        i = i+1
    return m

def printMatrix(m):
    for i in range(len(m)):
        print(m[i])


m = [['a1','b1','c1','d1'],
     ['a2','b2','c2','d2'],
     ['a3','b3','c3','d3'],
     ['a4','b4','c4','d4']]
m_=rotateMatrix(m)
printMatrix(m)