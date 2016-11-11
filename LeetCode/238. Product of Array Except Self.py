class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        l = len(nums)
        p = 1
        for i in range(0, l):
            answer.append(p)
            p = p * nums[i]
        p = 1
        for j in range(l-1, -1, -1):
            answer[j] = answer[j]* p
            p = p * nums[j]
        return answer