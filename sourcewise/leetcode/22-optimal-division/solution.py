class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return '%d/%d' % (nums[0], nums[1])
        from functools import reduce
        den = reduce(lambda acc, val: acc + '/' + str(val), nums[2:], str(nums[1]))
        return str(nums[0]) + '/(' + den + ')'
'''

class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        self.nums = nums

        return self.maxValue(0, len(nums)-1)

    def maxValue(self, i, j):
        if i == j:
            return str(self.nums[i])
        elif j == i+1:
            return '%d/%d' % (self.nums[i],self.nums[j])
        elif i < j:
            maxval = 0
            maxk = i
            bestnum = ''
            bestden = ''
            for k in range(i, j):
                num = self.maxValue(i, k)
                den = self.minValue(k+1, j)
                val = eval(num)/eval(den)
                if val > maxval:
                    maxval = val
                    bestnum = num
                    bestden = den
                    maxk = k
            if j - maxk >= 2:
                return bestnum + '/(' + bestden + ')'
            else:
                return bestnum + '/' + bestden
        else:
            raise Exception('Invalid case i:%d, j:%d, k:%d' % (i,j))

    def minValue(self, i, j):
        if i == j:
            return str(self.nums[i])
        elif j == i + 1:
            return '%d/%d' % (self.nums[i],self.nums[j])
        elif i < j:
            minval = 10E8
            mink = i
            bestnum = ''
            bestden = ''
            for k in range(i, j):
                num = self.minValue(i, k)
                den = self.maxValue(k + 1, j)
                val = eval(num) / eval(den)
                if val < minval:
                    minval = val
                    bestnum = num
                    bestden = den
                    mink = k
            if j - mink >= 2:
                return bestnum + '/(' + bestden + ')'
            else:
                return bestnum + '/' + bestden
        else:
            raise Exception('Invalid case i:%d, j:%d, k:%d' % (i, j))


if __name__ == '__main__':
    sln = Solution()
    nums = [1,777,133,861,416,482,796,33,299,643]
    print(sln.optimalDivision(nums))
'''
