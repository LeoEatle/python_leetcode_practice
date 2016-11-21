#coding: utf-8
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        minNum = nums[0]

        for num in nums:
            total = total + num
            minNum = min(num, minNum)
        diff = total - len(nums)*minNum
        return diff

s = Solution()
print s.minMoves([1,2,3])