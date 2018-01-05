class Solution:
    def convert(self, s):
        stack = [[s[0],-2]]
        for ch in s[1:]:
            if stack[-1] == ch:
                stack[-1][1] += 1
            else
                stack.append([ch, -2])
        return stack

    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        stack = self.convert(board)
        self.search(stack)

    def search(self, stack):
        if len(stack) == 1:
            elem = stack[0]
            val =  self.canbePopped(elem)
            if val == -1:
                return -1
            else:
                return val
        for i in range(len(stack)):
            val = self.canbePopped(stack[i])
            if val == -1:
                continue
            else:
                newstack = None
                if stack[i-1][0] == stack[i+1][0]:
                    newstack
                val = self.search(stack[:i] + stack[i+1:])

    def cabBePopped(self, elem):


if __name__ == '__main__':
    sln = Solution()
    print(sln.findMinStep("RBYYBBRRB", "YRBGB"))