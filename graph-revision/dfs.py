graph = {'A': ['B'],
         'B': ['D'],
         'C': [],
         'D': ['A']}

def dfs_helper(node, visited):
    visited[node] = 1
    print 'Visted ' + node
    for n in graph[node]:
        if visited[n] == 0:
            dfs_helper(n, visited)

def dfs(graph):
    visited = {node: 0 for node in graph}
    for node in graph:
        if visited[node] == 0:
            dfs_helper(node, visited)

dfs(graph)
