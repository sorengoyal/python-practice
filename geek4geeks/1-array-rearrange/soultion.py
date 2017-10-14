def rearrange(data):
    dfs(data)
    for i in range(0, len(data)):
        data[i] -= 100

def dfs(data):
    n = len(data)
    for i in range(0,n):
        if data[i] < 100 : #i is not vitied yet
            reserve = data[i]
            dfsHelper(data, i, reserve)


def dfsHelper(data, i, reserve):
    next = data[i]
    nextToNext = data[next]
    data[i] = data[next] + 100
    if(data[nextToNext] >= 100): #nextToNext is visited
        data[next] = reserve + 100
    else:
        dfsHelper(data, next, reserve)


T = int(input())
for t in range(0, T):
    n = int(input())
    line = input()
    chars = filter(lambda x: x != '', line.split(' '))
    data = list(map(lambda x: int(x), chars))
    rearrange(data)
    for e in data:
        print(e, end = ' ')
    print()
