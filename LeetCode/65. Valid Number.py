class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) is 0:
            return False
        numbers = ["0","1","2","3","4","5","6","7","8","9",".","e"]
        # e_flag = False
        # point_flag = False
        flag = False
        s = s.strip()#remove the blank char
        if len(s) == 0:
            return False
        if s[0] == '-':
            s = s[1:]
        if s == "." or s.count('.') > 1:
            return False
        print s
        if s[0] == 'e' or s[-1] == 'e':
            return False
        for i in range(len(s)):
            if (s[i] == 'e' or s[i] == '.') and flag == False:
                numbers.remove('e')
                numbers.remove('.')
                flag = True
                continue
            if not (s[i] in numbers):
                return False
        return True

#print '  34234  '.strip()
s = Solution()
print s.isNumber('  -234324e234  ')