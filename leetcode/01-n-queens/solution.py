class Solution(object):
    def __init__(self):
        self.configs = []

    def solveNQueens(self, n):
        b = [['o' for j in range(0, n)] for i in range(0, n)]
        self.collectConfigurations(b, 0)
        return self.configs

    def collectConfigurations(self, board, row):
        from functools import reduce
        n = len(board)
        for j in range(0, n):
            if board[row][j] == 'o':
                newboard = self.placeQueen(board, (row, j))
                if row == n - 1:
                    self.configs.append([ reduce(lambda s, elem: s+elem, r) for r in newboard])
                    continue
                self.collectConfigurations(newboard, row + 1)

    def placeQueen(self, board, point):
        newboard = [list(row) for row in board]
        n = len(board)
        for i in range(point[0], n):
            for j in range(0, n):
                if board[i][j] == '.':
                    continue
                if j == point[1] or i == point[0] or abs(i - point[0]) == abs(j - point[1]):
                    newboard[i][j] = '.'
                    continue
                #newboard[i][j] = 'o'
        newboard[point[0]][point[1]] = 'Q'
        return newboard

if __name__ == '__main__' :
    s = Solution()
    print(s.solveNQueens(4))




