class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0
        self.T = [[-1]*n for i in range(n)]
        self.A = A
        self.isArithmeticSlice(0,n-1)
        count = 0
        for i in range(n):
            for j in range(n):
                if self.T[i][j] == 1:
                    count += 1
        return count

    def isArithmeticSlice(self,i,j):
        T = self.T
        A = self.A
        if T[i][j] != -1:
            return T[i][j]
        if j - i == 2:
            T[i][j] = 0 if 2*A[i+1]-A[i]-A[j] else 1
            return T[i][j]
        elif j - i > 2:
            T[i][j] = 0 if self.isArithmeticSlice(i,j-1) + self.isArithmeticSlice(i+1,j) < 2 else 1
            return T[i][j]
        else:
            raise Exception('Invalid case')

if __name__ == '__main__':
    sln = Solution()
    print(sln.numberOfArithmeticSlices([1, 1, 2, 5, 7]))