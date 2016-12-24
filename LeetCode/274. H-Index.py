#coding: utf-8
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        bucket_list = []#bucket_list就是代表在那个index的paper的citaion数就是index的值
        l = len(citations)
        for i in range(l+1):
            bucket_list.append(0)
        for i in citations:
            if i >= l:
                bucket_list[l] += 1
            else:
                bucket_list[i] += 1
        j = l
        accumulate = 0
        while j > 0:
            accumulate = accumulate + bucket_list[j]
            if accumulate >= j:
                return j
            j-=1
        return 0

s = Solution()
print s.hIndex([3,0,6,1,5])
