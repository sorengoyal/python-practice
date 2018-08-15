class Solution:
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
            """
        #A = [[i*j for j in range(1,n+1)] for i in range(1,m+1)]

        def isBigEnough(x):
            val = sum([min(x//i, n) for i in range(1, m+1)])
            print(val)
            return val >= k

        lo = 1
        hi = m*n
        guess = (hi+lo)//2
        while(hi - lo > 0):
            if isBigEnough(guess):
                hi = guess
            else:
                lo = guess + 1
            guess = (hi+lo)//2
        return guess

if __name__ == '__main__' :
    sln = Solution()
    print(sln.findKthNumber(45,12,471))
