class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        carry = 0
        answer = ""
        if l1 > l2:
            longer = l1
        else:
            longer = l2
        #longer = l1 > l2 ? l1: l2
        for i in range(longer):
            if i <= l1:
                n1 = ord(num1[-i]) - ord('0')
            else:
                n1 = 0
            if i <= l2:
                n2 = ord(num2[-i]) - ord('0')
            else:
                n2 = 0
            s = n1 + n2 + carry
            if s / 10 == 1:
                carry = 1
            else:
                carry = 0
            answer = answer + str(s % 10)
        if carry == 1:
            answer = answer + '1'
        return answer[::-1]
        #return str(list(answer).reverse())

s = Solution()
print s.addStrings("9","99")
