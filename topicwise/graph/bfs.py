graph = {0: [1,2,3],
         1: [4,5,6],
         2: [],
         3: [],
         4: [],
         5: [],
         6: [1]}

def bfs(graph):
    q = [0]
    visited = [0]*len(graph)
    while len(q) != 0:
        n = q.pop()
        visited[n] = 1
        print(n)
        neighbors = graph[n]
        for i in neighbors:
            if visited[i] == 0:
                q.insert(0,i)

bfs(graph)