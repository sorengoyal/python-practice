class Solution(object):

    def maxCoins(self, data):
        n = len(data)
        if(len(data) == 1):
            return data[0]
        max = 0
        for i in range(0,n):
            l = self.localScore(data, i)
            newdata = data[:i] + data[i+1:]
            d = self.maxCoins(newdata)
            score = l + d
            if(max < score):
                max = score
        return max

    def localScore(self, data, i):
        if i == 0:
            return data[i]*data[i+1]
        elif i == len(data)-1:
            return data[i-1]*data[i]
        else:
            return data[i-1]*data[i]*data[i+1]


if __name__== '__main__':
    sln = Solution()
    print(sln.maxCoins([3,1,5,8]))

