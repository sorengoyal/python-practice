import heapq
class PancakeHouse:

    def solve(self):
        t = int(raw_input())
        for i in range(1,t+1):
            inp = raw_input()
            state, n, k = self.parse(inp)
            min = self.getMinPathLength(state, n, k)

            if min is None:
                print("Case #%d: Impossible" % i)
            else:
                print("Case #%d: %d" % (i, min))

    def parse(self, inp):
        state_str, k = inp.split(' ' )
        return self.convertToIndex(state_str), len(state_str), int(k)

    def transitions(self, state, n, k):
        mask = (2**k-1) << (n-k)
        for i in range(n-k+1):
            yield state^mask
            mask = mask >> 1

    def convertToIndex(self, state_str):
        index = 0
        for c in state_str:
            index = 2*index + (1 if c=='-' else 0)
        return index

    def getMinPathLength(self, state, n, k):
        minPathLength = [None] * (2 ** n)
        minPathLength[state] = 0
        q = [(minPathLength[state], state)]
        while len(q) > 0:
            pathLength, node = heapq.heappop(q)
            for transition in self.transitions(node, n, k):
                if minPathLength[transition] is None:
                    minPathLength[transition] = minPathLength[node] + 1
                    heapq.heappush(q, (minPathLength[transition], transition))
                else:
                    if minPathLength[transition] > minPathLength[node] + 1:
                        minPathLength[transition] = minPathLength[node] + 1
                        heapq.heappush(q, (minPathLength[transition], transition))
        return minPathLength[0]


if __name__ == '__main__':
    ph = PancakeHouse()
    ph.solve()

    '''state, n, k = ph.parse('-+-+- 4')
    min = ph.getMinPathLength(state, n, k)
    if min is None:
        print("Case #%d: Impossible" % 1)
    else:
        print("Case #%d: %d" % (1, min))
    '''