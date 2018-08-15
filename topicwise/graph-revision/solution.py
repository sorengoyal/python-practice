s = 'geeksfojrgeeksj'
r = 'geeksjgeeks'
N = len(s)
M = len(r)
isSub = [[None for j in range(M+1)] for i in range(N+1)]
for i in range(N+1):
    isSub[i][0] = True
for i in range(1,N+1):
    for j in range(1,M+1):
        if i < j:
            isSub[i][j] = False
        else:
            if s[i-1]==r[j-1]:
                isSub[i][j] = isSub[i-1][j-1]
            else:
                isSub[i][j] = isSub[i-1][j]
print(isSub[N][M])