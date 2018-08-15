class Solution:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        solo = [({i}, a) for (i, a) in enumerate(nums)]
        ops = [lambda x, y: x + y,
               lambda x, y: x * y,
               lambda x, y: x - y,
               lambda x, y: x / y if y > 0 else float('nan')]
        duos = [(i | j, op(a, b)) for (i, a) in solo for (j, b) in solo for op in ops if not (i & j)]
        duoduos = [op(a, b) for (i, a) in duos for (j, b) in duos for op in ops if not (i & j)]
        if 24 in duoduos:
            return True
        trios1 = [(i | j, op(a, b)) for (i, a) in duos for (j, b) in solo for op in ops if not (i & j)]
        trios2 = [(i | j, op(b, a)) for (i, a) in duos for (j, b) in solo for op in ops if not (i & j)]
        if 24 in [rec[1] for rec in trios1+trios2]:
            return True
        quads1 = [op(a, b) for (i, a) in trios1 + trios2 for (j, b) in solo for op in ops if not (i & j)]
        quads2 = [op(b, a) for (i, a) in trios1 + trios2 for (j, b) in solo for op in ops if not (i & j)]
        if 24 in quads1 + quads2:
            return True
        return False
if __name__ == '__main__':
    sln = Solution()
    print(sln.judgePoint24([3, 3, 8, 8]))