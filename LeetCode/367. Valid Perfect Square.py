#coding: utf-8
import math
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        cache = []
        return self.getDivision(num, cache)


    def getDivision(self, num, cache):
        limit = int(math.floor(num / 2))
        i = 2
        cache = 0
        flag = False
        while i <= limit:
            if num%i == 0:
                num = num / i
                if cache == i:
                    cache = 0
                    flag = True
                elif cache == 0:
                    cache = i
                else:
                    return False
            else:
                i = i + 1
        return flag

    def isPerfectSquare2(self, num):
        low = 1
        high = num

        while low <= high:
            mid = int((low + high) / 2)
            if mid * mid == num:
                return True

            elif mid * mid > num:
                high = int(mid - 1)
            elif mid * mid < num:
                low = int(mid + 1)
        return False


s = Solution()
print s.isPerfectSquare2(2147483647)

