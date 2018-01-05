class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        iX = 0
        iO = len(nums)-1
        iN = (iX + iO)//2
        while iX < iO :
            X = nums[iX]
            O = nums[iO]
            N = nums[iN]
            if X == O:
                iX = iX+1
            elif X <= N and N <= O:
                iN = iX
                break
            elif N <= X and N <=O:
                iO = iN
            elif N >= X and N >= O:
                iX = iN+1
            else:
                print("invalid case")
            iN = (iX + iO) // 2
        return nums[iN]

def pivot(l, p):
    n = len(l)
    return [l[(i+p)%n] for i in range(0,n)]
if __name__ == '__main__':
    sln = Solution()
    l = list(range(0,100))
    l = list(range(0,10))
    print(sln.findMin([1,3,3]))
    #for i in l:
    #    print(sln.findMin(pivot(l,i)))