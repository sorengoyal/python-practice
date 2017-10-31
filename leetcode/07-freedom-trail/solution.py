class Solution:
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        self.ring = ring
        indexMap = self.buildIndexMap()
        n = len(key)
        m = len(self.ring)
        c = [ [0 for j in range(0,m)] for i in range(0,n+1)]
        s = [ [0 for j in range(0,m)] for i in range(0,m)]
        for r in range(0,m):
            for r1 in range(0,m):
                s[r][r1] = self.getSteps(r,r1)
        for k in range(n-1, -1, -1):
            for r in range(0, m):
                c[k][r] = min([c[k+1][i] + s[r][i] + 1 for i in indexMap[key[k]]])
        return c[0][0]

    def buildIndexMap(self):
        d = {}
        for i,c in enumerate(self.ring):
            if c not in d:
                d[c] = [i]
            else:
                d[c] += [i]
        return d

    def getSteps(self, r, r1):
        m = len(self.ring)
        if abs(r1-r) <= m/2:
            return abs(r1-r)
        else:
            return m - abs(r1-r)

if __name__ == '__main__':
    sln = Solution()
    ring = "uhkmmysrhsdexzosvjckhmepx"
    key = "eeossmhkschhohucxujosvedukscjrmesmsmkkkmzxsjrmhdkheduzchrppevmxmsrxxkzexjhzkphsyhmssdxmvhhoxypevmymy"
    s = sln.findRotateSteps(ring, key)
    print(s)