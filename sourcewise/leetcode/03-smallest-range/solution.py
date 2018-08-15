class Interval:
    def __init__(self, a, b):
        if a > b:
            raise Exception
        self.a = a
        self.b = b

    def length(self):
        return b-a

    def covers(self, L):

class Solution:
    coverMatrix = []
    inf = 10 ** 6
    R1 = {}
    R2 = {}
    def smallestRange(self, nums):
        self.LL = nums
        a = min([L[0] for L in nums])
        b = max([L[-1] for L in nums])
        return self.L(a,b)

    def L(self, a, b):
        if a > b:
            return self.inf
        if a < -10**5 or a > 10**5 or b < 10**5 or b > 10**5:
            return self.inf
        r1 = self.getR1(a)
        r2 = self.getR2(b)
        if I.covers()
    def buildR1(self, a):
        if a in self.R1:
            return self.R1[a]
        mins = []
        for L in self.LL:
            fl = filter(lambda x: x>=a, L)
            x = min(fl)

    def buildCoverMatrix(self):



    def updateInterval(self, x1, x2, I, nums):
        I1 = []
        for s,i in zip(nums, I):
            p = i[0]
            while s[p] <= x1:
                p = p + 1
                if p == 0:
                    p = None
                    break
            q = i[1]
            while s[q] >= x2:
                q = q - 1
                if q == 0:
                    q = None
                    break
            if p is None or q is None:
                I1.append(None)
            else:
                I1.append((p,q))
        return I1

    def L(self, x1, x2, I, nums):
        if self.isInvalid(I):
            return self.inf
        min = x2-x1
        for r1,s1 in zip([i[0] for i in I],nums):
            for r2,s2 in zip([i[1] for i in I],nums):
                I1 = self.updateInterval(s1[r1], s2[r2], I, nums)
                val = self.L(s1[r1], s2[r2], I1, nums)
                if min > val:
                    min = val
        return min


if __name__ == '__main__':
    sln = Solution()
    print(sln.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))