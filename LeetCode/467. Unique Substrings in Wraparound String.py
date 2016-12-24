#coding: utf-8
import collections
class Solution(object):
    # def findSubstringInWraproundString(self, p):
    #     """
    #     :type p: str
    #     :rtype: int
    #     """
    #     l = len(p)
    #     count = 0
    #     unique = set()
    #     for i in range(l):
    #         j = i
    #
    #         if p[i] in unique:
    #             pass
    #         else:
    #             count += 1
    #             unique.add(p[i])
    #
    #         cache = [p[i]]
    #         while j < l-1:
    #             if self.checkS(p[j], p[j+1]):
    #                 cache.append(p[j+1])
    #                 if str(cache) in unique:
    #                     j+=1
    #                     pass
    #                 else:
    #                     count+=1
    #                     unique.add(str(cache))
    #                     j+=1
    #             else:
    #                 break
    #
    #     return count

    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        unique = collections.defaultdict(int)
        l = len(p)
        maxLen = 0
        for i in range(l):

            if i and not self.checkS(p[i-1], p[i]):
                maxLen = 1
            else:
                maxLen = maxLen + 1
            unique[p[i]] = max(maxLen, unique[p[i]])
        return sum(unique.values())






    def checkS(self, a, b):
        if ord(b) == ord(a) + 1 or ord(b) == ord(a) - 25:
            return True

s = Solution()
#print s.checkS('z','a')
print s.findSubstringInWraproundString('abaab')
