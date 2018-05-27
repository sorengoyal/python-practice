class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [list(nums)]
        l = []
        nums = set(nums)
        for val in nums:
            perms = self.permute(nums - {val})
            for perm in perms:
                l.append([val] + perm)
        return l

if __name__ == '__main__':
    sln = Solution()
    print(len(sln.permute([1,2,3,4])))