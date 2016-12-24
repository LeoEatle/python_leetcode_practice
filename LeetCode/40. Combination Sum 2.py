#coding: utf-8
import copy
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l = len(candidates)
        if l <= 0:
            return 0
        candidates.sort()
        candidates.reverse()
        self.target = target
        self.result = 0
        self.answer = []
        self.find(candidates, target, [])
        return self.answer

    def find(self, candidates, target, cache):
        index = 0
        while(index<len(candidates)):
            #target = target - i
            i = candidates[index]
            if target-i == 0:
                self.result +=1
                cache.append(i)
                self.answer.append(cache)
                break
                #return
                #candidates.remove(i)
            elif target-i < 0:
                candidates.remove(i)
                continue
            elif target-i > 0:

                cache.append(i)
                candidates.remove(i)
                origin_candidates = copy.copy(candidates)
                self.find(origin_candidates, target-i, cache)



s = Solution()
print s.combinationSum2([10,1,2,7,6,1,5], 8)
