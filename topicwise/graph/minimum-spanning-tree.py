
graph = [[0,1,5,0],
         [0,0,2,0],
         [0,0,0,3],
         [4,6,0,0]]
def prim(graph):
    n = len(graph)
    V = set([0])
    V_ = set(range(1,n))
    E = set()
    E_ = set()
    for u in range(n):
        for v in range(n):
            if graph[u][v] != 0:
                E_.add((u,v))
    print(E_)
    while len(V_) != 0:
        min = 1000
        minedge = (None,None)
        for (u,v) in E_:
            if graph[u][v] < min:
                min = graph[u][v]
                minedge = (u,v)
        E.add(minedge)
        E_.remove(minedge)
        V.add(minedge[1])
        V_.remove(minedge[1])
    print(E)


prim(graph)