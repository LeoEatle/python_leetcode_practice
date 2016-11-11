# coding: utf-8

number = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
n = raw_input()
n = int(n)
for i in range(n):
    s = raw_input()
    i = number.index(s)
    if i >= 8:
        print i - 8
    else:
        print i - 8 + 10