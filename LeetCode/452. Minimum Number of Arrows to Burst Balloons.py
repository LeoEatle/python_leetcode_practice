#coding : utf-8
class Solution(object):
    def findMinArrowShots(self, points):
        points = sorted(points, key = lambda x: x[1])
        res, end = 0, -float('inf')#赋值负无穷
        for interval in points:
            if interval[0] > end:
                res += 1
                end = interval[0]
        return res
