g = {0: [1],
     1: [2],
     2: [0,3],
     3: [2]}

time = 1

def dfs_helper(i, graph, starttime, fintime):
    global time
    starttime[i] = time
    print(str(i) + ':' + str((starttime, fintime)))
    time = time + 1
    neigh = g.get(i)
    for n in neigh:
        if starttime[n] != 0 and fintime[n] == 0:
            print("Cycle exists")
        if starttime[n] == 0:
            dfs_helper(n, graph, starttime, fintime)
    fintime[i] = time
    time = time+1

def dfs(graph):
    n = len(graph)
    visited = [0]*n
    starttime = [0]*n
    fintime = [0]*n
    global time
    time = 1
    for i in range(n):
        if starttime[i] == 0:
            dfs_helper(i, graph, starttime, fintime)

dfs(g)
print(g)