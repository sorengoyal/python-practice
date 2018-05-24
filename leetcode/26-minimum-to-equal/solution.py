class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        if n%2 == 1:
            m = int(n/2)
            median = nums[m]
        else:
            median = int((nums[n/2] + nums[n/2+1])/2)
        sum1 = 0
        for v in nums:
            sum1 += abs(median - v)
        return sum1
