graph = {'A': ['B', 'D'],
         'B': ['C','E'],
         'C': [],
         'D': ['A'],
         'E': []}
def dfs_helper(node, graph, visited):
    visited[node] = True
    print('visited ' + node)
    for child in graph[node]:
        if not visited[child]:
            dfs_helper(child, graph, visited)

def dfs(graph):
    V = len(graph)
    visited = {node: False for node in graph}
    for node in visited:
        if not visited[node]:
            dfs_helper(node, graph, visited)

dfs(graph)
