class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # using Dp solution
        dp = [1,9]

        for i in range(2,11):
            #if i == 2:
            #    dp.append(9*9)
            dp.append(dp[-1] * (11-i))
        print dp
        result = 0
        for j in range(n+1):
            if j > 10:
                return result
            result = result + dp[j]
        return result

s = Solution()
print s.countNumbersWithUniqueDigits(3)