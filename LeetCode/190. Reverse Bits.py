#coding: utf-8
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binStr = bin(n)[2:]
        reverseArr = []
        for i in binStr:
            reverseArr.append(i)
        while len(reverseArr)<32:
            reverseArr.insert(0,"0")
        reverseArr.reverse()
        answer = ""
        for j in reverseArr:
            answer = answer+j
        print answer
        return int(answer,2)

    def reverseBits_1(self, n):
        reversed = 0
        for i in range(32):
            reversed = reversed << 1
            print reversed
            reversed |= (n >> i) & 0x1
            print reversed
        return reversed

print Solution().reverseBits_1(43261596)