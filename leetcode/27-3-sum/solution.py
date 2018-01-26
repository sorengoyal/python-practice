data = {}

class Solution:

    class NaryNode:

        def __init__(self, val, set):
            self.children = []
            self.val = val
            self.set = set + [val]

        def insert(self, val):
            if len(self.set) <= 1:
                for node in self.children:
                        node.insert(val)
            node = Solution.NaryNode(val, self.set)
            self.children.append(node)
            if sum(node.set) == 0:
                data[tuple(set(node.set))] = node.set

        def __str__(self):
            return str(self.val) + ',' + str([node.__str__() for node in self.children])

    def solutionSet(self,l):
        head = []
        self.solution = {}
        for val in l:
            for children in head:
                children.insert(val)
            head.append(self.NaryNode(val, []))
            for children in head:
                print(children)
            print('inserted %d' % val)
        print(data)


if __name__ == '__main__':
    sln = Solution()
    l = [-1, 0, -1, 2]
    print(sln.solutionSet(l))