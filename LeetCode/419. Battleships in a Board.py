class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        x = len(board[0])
        y = len(board)
        count = 0
        for i in xrange(y):
            for j in xrange(x):
                if board == "X" and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    count +=1
        return count

s = Solution()
print s.countBattleships(["X..X","...X","...X"])