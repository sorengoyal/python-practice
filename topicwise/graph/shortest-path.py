graph = [[0,2,2,3,0,0],
         [0,0,0,1,0,0],
         [0,0,0,0,1,0],
         [0,0,0,0,0,1],
         [0,0,0,0,0,1],
         [0,0,0,0,0,0]]
n = len(graph)
s = 0
t = 5
shortest_cache = [-1]*n

def shortest(v):
    if v == s:
        return 0
    if shortest_cache[v] == -1:
        min = 1000
        for u in range(n):
            if graph[u][v] != 0 and min > shortest(u) + graph[u][v]:
                min = shortest(u) + graph[u][v]
        shortest_cache[v] = min
    return shortest_cache[v]

print(shortest(t))
print(shortest_cache)