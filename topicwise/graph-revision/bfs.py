def bfs(graph):
    visited = {node: False for node in graph}
    stack = []
    stack.append(graph.keys()[0])
    while len(stack) != 0:
        node = stack.pop()
        visited[node] = True
        print('visited ' + node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                stack.append(neighbor)
graph = {'A': ['B', 'D'],
         'B': ['C','E'],
         'C': [],
         'D': ['A'],
         'E': []}

bfs(graph)