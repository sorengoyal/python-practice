class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [1]*n
        forwardProduct = 1
        for i in range(0,n):
            output[i] = forwardProduct
            forwardProduct *= nums[i]

        backwardProduct = 1
        for i in range(n-1, -1, -1):
            output[i] *= backwardProduct
            backwardProduct *= nums[i]

        return output


if __name__ == '__main__':
    sln = Solution()
    print(sln.productExceptSelf([1,2,3,4]))