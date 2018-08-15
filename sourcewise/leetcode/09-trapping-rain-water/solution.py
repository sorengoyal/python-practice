class Solution:
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        w = len(heightMap)
        if w <= 1:
            return 0
        l = len(heightMap[0])
        if w*l <= 1:
            return 0
        h = self.getMaxHeight(heightMap)
        volume = 0
        grid = [[['unassigned' for j in range(l)] for i in range(w)] for k in range(h)]
        for level, layer in enumerate(grid):
            self.populateLayer(layer, heightMap, level)
            for i in range(w):
                for j in range(l):

                    if self.willDrainout(layer, i, j) == 'no':
                        volume = volume + 1
        return volume

    def populateLayer(self, layer, heightMap, level):
        w = len(heightMap)
        l = len(heightMap[0])
        for i in range(w):
            for j in range(l):
                if level+1 <= heightMap[i][j]:
                    layer[i][j] = 'occupied'

    def willDrainout(self, layer, i, j):
        w = len(layer)
        l = len(layer[0])
        if i < 0 or j < 0 or i == w or j == l:
            return 'yes'
        if layer[i][j] != 'unassigned':
            return layer[i][j]
        layer[i][j] = 'cannot say'
        if self.willDrainout(layer, i-1, j) == 'yes':
            layer[i][j] = 'yes'
            return 'yes'
        if self.willDrainout(layer, i, j - 1) == 'yes':
            layer[i][j] = 'yes'
            return 'yes'
        if self.willDrainout(layer, i+1, j) == 'yes':
            layer[i][j] = 'yes'
            return 'yes'
        if self.willDrainout(layer, i, j+1) == 'yes':
            layer[i][j] = 'yes'
            return 'yes'
        layer[i][j] = 'no'
        return 'no'

    def getMaxHeight(self, heightMap):
        maxx = heightMap[0][0]
        for row in heightMap:
            for e in row:
                if maxx < e:
                    maxx = e
        return maxx

if __name__ == '__main__':
    sln = Solution()
    #print(sln.trapRainWater([]))
    #print(sln.trapRainWater([[2,1,2]]))
    #print(sln.trapRainWater([[2,2,2], [2,1,2], [2,2,2]]))
    #print(sln.trapRainWater([[2, 1, 2], [2, 3, 2], [2, 1, 2]]))
    #print(sln.trapRainWater([[2, 2, 2, 2, 2], [2, 1, 1, 1, 2], [2, 1, 3, 1, 2], [2, 1, 1, 1, 2], [2, 2, 2, 2, 2]]))
    #print(sln.trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))
    print(sln.trapRainWater([[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]))