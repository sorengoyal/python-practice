import random

class Graph:
    def __init__(self):
        self.matrix = self.generateRandomGraph(5)

    def __init__(self, matrix):
        self.matrix = matrix

    def getNumOfNodes(self):
        return len(self.matrix)
    def getAdjacenyListRepresentation(self):
        g = {}
        n = len(self.matrix)
        for i in range(n):
            g[i] = set()
            for j in range(n):
                if self.matrix[i][j] == 1:
                    g[i].add(j)
        return g

    def getMatrixRepresentation(self):
        return self.matrix

    def generateRandomGraph(self, n):
        self.matrix = [[random.randint(0,1) for i in range(n)] for j in range(n)]

    def __str__(self):
        l = self.getAdjacenyListRepresentation()
        s = ''
        for node in l:
            s += str(node) + ': ' + str(l[node]) + '\n'
        return s

