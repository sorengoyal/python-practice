class Solution:
    def sumOfBitDifference(self, l):
        count = 0
        sum = 0
        N = len(l)
        for i in range(32):
            for j, elem in enumerate(l):
                count += elem & 0b1
                l[j] = elem >> 1
            sum += count*(N-count)*2
            count = 0

        return sum

if __name__ == '__main__':
    sln = Solution()
    print(sln.sumOfBitDifference([1,3,5]))