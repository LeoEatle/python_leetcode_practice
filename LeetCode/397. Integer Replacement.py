class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n is not 1:
            if n % 2 == 0:
                n = n / 2
                count += 1
            elif n == 3 or n & 3 == 1:
                n = n - 1
                count += 1
            else:
                n = n + 1
                count += 1
        return count
