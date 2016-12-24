class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        Index = 0
        length = len(A)
        if length == 0:
            return 0
        total = 0
        for i in range(length):
            total = total + i*A[i]
        result = total
        addSum = sum(A)
        FValues = [total]
        answer = 0

        for i in range(1,length):
            result = result + addSum - length * A[-i]
            FValues.append(result)

        print FValues
        return  max(FValues)

s = Solution()
print s.maxRotateFunction([4,3,2,6])
