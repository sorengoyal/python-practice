class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0
        count = 0
        inc = 1
        for i in range(2, n):
            if 2*A[i-1] - A[i-2] - A[i]:
                inc = 1
            else:
                count += inc
                inc += 1

        return count

if __name__ == '__main__':
    sln = Solution()
    print(sln.numberOfArithmeticSlices([1, 2, 3, 4, 5, 7, 9]))