#coding: utf-8

#输入一个n 和一个m,从n个字符串中进行字典序排序,如n是11,就是[1,10,11,2,3,4,5,6,7,8,9],
# 找到第m个,假如m是4,结果就是2

s = raw_input()
if s != "":
    n = int(s.split(" ")[0])
    m = int(s.split(" ")[1])
    l1 = []
    l2 = []
    for i in range(1, n+1):
        l1.append(str(i))
    l1.sort()
    print l1[m - 1]