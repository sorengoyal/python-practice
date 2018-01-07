class Solution:
    from queue import PriorityQueue

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        data = self.PriorityQueue()
        [data.put([-p[0]*100+p[1]] + p) for p in people]
        q = []
        while not data.empty():
            n, h, k = data.get()
            p = self.getPosition(q, h, k)
            if p == -1:
                data.put([n+1,h,k])
            else:
                q.insert(p,[h,k])
        return q

    def getPosition(self, q, h, k):
        n = len(q)
        if n == 0 :
            if k == 0:
                return 0
            else:
                return -1
        count = 0
        for i in range(n):
            if k == count and h <= q[i][0]:
                return i
            if h <= q[i][0]:
                count += 1
        if k == count:
            return n
        return -1


if __name__ == '__main__':
    sln = Solution()
    people = [[1,4],[9,0],[6,1],[4,0],[3,3],[2,8],[7,1],[7,0],[6,4],[5,3]]
    print(sln.reconstructQueue(people))
