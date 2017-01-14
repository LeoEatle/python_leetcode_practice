#coding: utf-8
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        if target < matrix[0][0]:
            return False
        y = len(matrix)
        x = len(matrix[0])
        for i in range(y):
            if i == y-1 or target < matrix[i+1][0]:
                for j in range(x):
                    if target == matrix[i][j]:
                        return True

        return False