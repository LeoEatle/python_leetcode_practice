#coding: utf-8
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n!=1:
            if n in s:
                return False
            s.add(n)
            n = self.calculate(n)
        return True

    def calculate(self, n):
        total = 0
        for i in str(n):
            total = total + int(i)**2
        return total

s = Solution()
print s.isHappy(19)