class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        head = 0
        tail = len(s)-1
        while head < tail:
            if not s[head].isalnum():
                head+=1
                continue
            elif not s[tail].isalnum():
                tail-=1
                continue
            elif s[head].lower() == s[tail].lower():
                head+=1
                tail-=1
                continue
            elif s[head].lower() != s[tail].lower():
                return False
        return True

s = Solution()
print s.isPalindrome("A man, a plan, a canal: Panama")
