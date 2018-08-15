class SummaryRanges:
    class Interval:
        def __init__(self, s, e):
            self.start = s
            self.end = e
            self.next = None
            self.previous = None
            self.isFull = False

        def contains(self, val):
            return self.start <= val <= self.end

        def __repr__(self):
            return '[%d, %d]'% (self.start, self.end)
    inf = 10**7

    def __init__(self):
        self.head = self.Interval(-self.inf, self.inf)
        self.head.previous = self.Interval(-self.inf, -self.inf)
        self.head.next = self.Interval(self.inf, self.inf)

    def addNum(self, val):

        """
        :type val: int
        :rtype: void
        """
        p = self.head
        while not p.contains(val):
            p = p.next
        assert(p.contains(val))
        if p.isFull:
            return
        else:
            self.insertNode(p, val)

    def insertNode(self, p, val):
        prev = p.previous
        next = p.next
        if val == prev.end+1 and val == next.start-1:
            prev.end = next.end
            prev.next = next.next
            prev.next.previous = prev
        elif val == prev.end+1:
            prev.end = val
            p.start = val+1
        elif val == next.start-1:
            next.start = val
            p.end = val-1
        else:
            valnode = self.Interval(val, val)
            valnode.isFull = True
            q = self.Interval(val + 1, p.end)
            p.end = val-1
            p.next = valnode
            valnode.next = q
            q.next = next
            next.previous = q
            q.previous = valnode
            valnode.previous = p


    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        p = self.head
        l = []
        while p.next is not None:
            if p.isFull:
                l.append(p)
            p = p.next
        return l

if __name__ == '__main__':
    # Your SummaryRanges object will be instantiated and called as such:
    obj = SummaryRanges()
    obj.addNum(1)
    print(obj.getIntervals())
    obj.addNum(4)
    print(obj.getIntervals())
    obj.addNum(2)
    print(obj.getIntervals())
    obj.addNum(3)
    print(obj.getIntervals())