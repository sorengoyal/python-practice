class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return nums[0]
        if n == 2:
            if nums[0] == nums[1]:
                return -1
            raise Exception('Length two arrays cannothave uniqu values')
        m = int(n/2)
        if self.isUnique(nums, m):
            return nums[m]
        b = self.getBoundary(nums, m)
        l = self.singleNonDuplicate(nums[:b])
        if l != -1:
            return l
        return self.singleNonDuplicate(nums[b:])

    def isUnique(self, nums, i):
        #print(nums)
        if i == 0 or i == len(nums)-1:
            raise Exception('Border element being check for uniqueness')
        return nums[i-1] != nums[i] and nums[i] != nums[i+1]

    def getBoundary(self, nums, i):
        if i == 0 or i == len(nums)-1:
            raise Exception('Border element being used in getBoundary')
        if nums[i] == nums[i-1]:
            return i+1
        elif nums[i] == nums[i+1]:
            return i
        else:
            return i

if __name__ == '__main__':
    sln = Solution()
    l = [3,3,7,7,10,11,11]
    print(sln.singleNonDuplicate(l))
