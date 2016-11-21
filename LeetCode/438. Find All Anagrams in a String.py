#this code use coding: utf-8
import collections
class Solution(object):
    def findAnagrams2(self, s, p):
        sLength = len(s)
        pLength = len(p)
        answer = []



        for i in xrange(sLength-pLength+1):
            flag = 1
            temp = list(p)
            for j in s[i:i+pLength]:

                if temp.count(j) != 0:
                    temp.remove(j)
                else:
                    flag = 0
                    break
            if flag == 1:
                answer.append(i)
        return  answer

    def findAnagrams(self, s, p):
        sLength = len(s)
        pLength = len(p)
        if sLength < pLength:
            return []
        answer = []
        slicingWindow = collections.defaultdict(int)
        for i in range(pLength):
            slicingWindow[p[i]] = -1  # initialize the slicing window
        for j in range(sLength):
            if j < pLength:
                slicingWindow[s[j]] += 1
                if not slicingWindow[s[j]]: del slicingWindow[s[j]]

            else:
                if not slicingWindow: answer.append(j - pLength)

                slicingWindow[s[j - pLength]] -= 1
                if not slicingWindow[s[j - pLength]]: del slicingWindow[s[j - pLength]]
                slicingWindow[s[j]] += 1
                if not slicingWindow[s[j]]: del slicingWindow[s[j]]
        if not slicingWindow: answer.append(j - pLength + 1)

        return answer


s = Solution()
print s.findAnagrams("abab","ab")



