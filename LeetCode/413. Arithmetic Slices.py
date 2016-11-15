#coding: utf-8
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        cur = 0
        total = 0
        if len(A) < 3:
            return total
        for i in range(2, len(A)):
            if  A[i]-A[i-1] == A[i-1]-A[i-2]:
                cur = cur + 1
                total = total + cur
            else:
                cur = 0
        return total

s = Solution()
print s.numberOfArithmeticSlices([1,2,3,4])

