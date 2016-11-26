#coding: utf-8

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        y = len(board)
        x = len(board[0])
        edgePoint = []

        #遍历加入边缘的O点,并将遍历过的边上的点置为'S'
        for i in range(x):
            if board[0][i] == 'O':
                board[0][i] = 'S'
                edgePoint.append([0, i])
            if board[y-1][i] == 'O':
                board[y-1][i] = 'S'
                edgePoint.append([y-1, i])

        for j in range(y):
            if board[j][0] == 'O':
                board[j][0] = 'S'
                edgePoint.append([j, 0])
            if board[j][x-1] == 'O':
                board[j][x-1] = 'S'
                edgePoint.append([j, x-1])

        #遍历检查边缘O点是否有临近O点
        while len(edgePoint) > 0:
            temp = edgePoint.pop(0)
            tempX = temp[1]
            tempY = temp[0]
            if tempX-1 >= 0 and board[tempY][tempX-1] == 'O':
                board[tempY][tempX - 1] = 'S'
                edgePoint.append([tempY, tempX-1])
            if tempY-1 >= 0 and board[tempY-1][tempX] == 'O':
                board[tempY - 1][tempX] = 'S'
                edgePoint.append([tempY-1, tempX])
            if tempX+1 <= x-1 and board[tempY][tempX+1] == 'O':
                board[tempY][tempX + 1] = 'S'
                edgePoint.append([tempY, tempX+1])
            if tempY+1 <= y-1 and board[tempY+1][tempX] == 'O':
                board[tempY + 1][tempX] = 'S'
                edgePoint.append([tempY+1, tempX])

        for i in range(x):
            for j in range(y):
                if board[j][i] == 'O':
                    board[j][i] = 'X'
                elif board[j][i] == 'S':
                    board[j][i] = 'O'


s = Solution()
s.solve([['O','O','O'],['O','O','O'],['O','O','O']])
