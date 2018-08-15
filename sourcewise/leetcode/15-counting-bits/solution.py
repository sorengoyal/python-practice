class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        if num == 1:
            return [0,1]
        counts = [0,1]
        flag = 1
        for i in range(2,num+1):
            if i%flag == 0:
                counts.append(1)
                flag *= 2
            else:
                counts.append(1+counts[i-flag])
        return counts

if __name__ == '__main__':
    sln = Solution()
    print(sln.countBits(5))