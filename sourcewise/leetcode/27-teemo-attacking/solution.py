class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        poisonedUntilTime = 0
        totalPoisonTime = 0
        for t in timeSeries:
            totalPoisonTime += duration if t > poisonedUntilTime else t + duration - poisonedUntilTime
            poisonedUntilTime = t + duration
        return totalPoisonTime

if __name__ == '__main__':
    sln = Solution()
    print(sln.findPoisonedDuration([1,2],2))
