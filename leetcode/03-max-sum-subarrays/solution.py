class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        sumOfAllSubarrays = self.getSumOfAllSubarrays(nums, k)
        return self.getMaxSum(k=k, c=3, l=sumOfAllSubarrays)

    def getSumOfAllSubarrays(self, nums, k):
        sums = []
        sums.append(sum(nums[:k]))
        for i in range(1, len(nums)+1-k):
            val = sums[i-1] - nums[i-1] + nums[i-1+k]
            sums.append(val)
        return sums

    def getMaxSum(self, k, c, l):
        n = len(l)-1+k
        maxsum = [[0]*3 for i in range(0,n-k+1)]
        maxindices = [[[]]*3 for i in range(0,n-k+1)]
        for c in range(0,3):
            for i in range(n-(c+1)*k,-1,-1):
                if c == 0:
                    maxval = 0
                    maxindex = None
                    for j in range(n-k, i - 1, -1):
                        if maxval < l[j]:
                            maxval = l[j]
                            maxindex = j
                    maxsum[i][c] = maxval
                    maxindices[i][c] = [maxindex]
                else:
                    maxval = 0
                    maxindex = None
                    for j in range(n-(c+1)*k,i-1,-1):
                        sum = l[j] + maxsum[j+k][c-1]
                        if maxval < sum:
                            maxval = sum
                            maxindex = j
                    maxsum[i][c] = maxval
                    maxindices[i][c] = [maxindex] + maxindices[maxindex+k][c-1]
        return maxindices[0][2]


if __name__ == '__main__':
    sln = Solution()
    l = sln.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2)
    print(l)