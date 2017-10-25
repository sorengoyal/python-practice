class Solution:
    inf = 10 ** 6
    def smallestRange(self, nums):
        a = min([s[0] for s in nums])
        b = max([s[-1] for s in nums])
        I = [(0,len(s)-1) for s in nums]
        return self.L(a,b, I, nums)

    def isInvalid(self, I):
        return [i for i in I if i is None]

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