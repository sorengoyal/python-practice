class Solution:
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        self.ring = ring
        self.key = key
        self.indexMap = self.buildIndexMap()

        return self.countSteps(0,0)

    def countSteps(self, k, r):
        n = len(self.key)
        if k >= n:
            return 0
        minv = 1000
        for i in self.indexMap[self.key[k]]:
            steps = self.countSteps(k + 1, i) + self.getSteps(r, i) + 1
            if minv > steps:
                minv = steps
        return minv

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
    ring = "godding"
    key = "gd"
    s = sln.findRotateSteps(ring, key)
    print(s)