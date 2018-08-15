class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                elif board[i][j] == 'X':
                    if i == 0 and j == 0:
                        count += 1
                    elif i != 0 and j == 0:
                        if board[i-1][j] == '.':
                            count += 1
                    elif i == 0 and j !=0:
                        if board[i][j-1] == '.':
                            count += 1
                    elif i != 0 and j != 0:
                        if board[i-1][j] == '.' and board[i][j-1] == '.':
                            count += 1
        return count

if __name__ == '__main__':
    sln = Solution()
    board = [
        ['X', '.', '.', 'X'],
        ['.', '.', '.', 'X'],
        ['.', '.', '.', 'X']
    ]
    print(sln.countBattleships(board))
