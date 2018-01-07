class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 1:
            return []
        dupes = []
        ioa = self.ioa
        for i in range(1, n+1):
            #print('for' + str(nums))
            if ioa(nums,i) == i:
                continue
            elif ioa(nums,i) == 0:
                continue
            else:
                while ioa(nums, i) != 0 and ioa(nums, i) != i:
                    #print('while' + str(nums))
                    if ioa(nums, ioa(nums, i)) == ioa(nums, i):
                        dupes.append(ioa(nums, i))
                        self.ioaSet(nums, ioa(nums, i), 0)
                        self.ioaSet(nums, i, 0)
                        break
                    else:
                        self.swap(nums, i, ioa(nums, i))
        return dupes

    def swap(self, l, i, j):
        temp = self.ioa(l, i)
        self.ioaSet(l, i, self.ioa(l, j))
        self.ioaSet(l, j, temp)

    def ioa(self, l, i): #index 1 array
        if i == 0:
            raise Exception('Invalid index')
        return l[i-1]

    def ioaSet(self, l, i, val):
        if i == 0:
            raise Exception('Invalid index')
        l[i-1] = val

if __name__ == '__main__':
    sln = Solution()
    print(sln.findDuplicates([4,3,2,7,8,2,3,1]))