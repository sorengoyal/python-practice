class Solution:
    def findSubarray(self, f, c):
        n = len(f)
        h = [f[0]]
        h_ = {f[0]: 0}
        for x in range(1, n):
            h.append(h[x-1]+f[x])
            h_[h[x]] = x
        for a in range(n):
            if (c+h[a]-f[a]) in h_ and h_[c+h[a]-f[a]] > a:
                return a+1, h_[c+h[a]-f[a]]+1
        return -1


sln = Solution()
t = int(input())
for i in range(t):
    n, sum = [int(val) for val in input().split(' ')]
    if n == 0:
        input()
    else:
        l = [int(val) for val in input().strip().split(' ')]
    result = sln.findSubarray(l, sum)
    if result != -1:
        print("%d %d"% result)
    else:
        print(-1)


