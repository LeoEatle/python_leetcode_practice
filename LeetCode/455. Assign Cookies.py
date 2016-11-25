#coding: utf-8
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count = 0
        for i in g:
            flag = 0
            for j in s:
                if j >= i:
                    flag = 1
                    s.remove(j)
                    break
            if flag == 1:
                count += 1
        return count

instance = Solution()
print instance.findContentChildren([1,2],[1,2,3])