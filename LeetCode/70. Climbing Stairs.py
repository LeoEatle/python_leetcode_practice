#coding: utf-8
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ways = 0
        self.countWays(n)
        return self.ways

    def countWays(self, n):
        if n < 0:
            return
        if n == 0:
            self.ways = self.ways + 1
            return
        self.countWays(n-1)
        self.countWays(n-2)


class Solution1(object):
    def climbStairs(self, n):
        if n < 1:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev1 = 0
        prev2 = 1
        for i in range(n):
            now = prev1+prev2
            prev1 = prev2
            prev2 = now
        return now


s = Solution1()
print s.climbStairs(3)

