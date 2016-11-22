#coding: utf-8
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #without extra space and in O(n) time
        answer = []
        for i in nums:
            i = abs(i)
            if nums[i-1]> 0:
                nums[i-1] = -nums[i-1]
        for j in range(len(nums)):
            if nums[j] > 0:
                answer.append(j+1)
        return answer

        # nums.sort()
        # answer = []
        # for i in range(len(nums)):
        #     if nums[i] != i+1:
        #         answer.append(i)
        # return answer

s = Solution()
print s.findDisappearedNumbers([4,3,2,7,8,2,3,1])