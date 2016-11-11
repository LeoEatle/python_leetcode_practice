# coding: utf-8

n = raw_input()
n = int(n)
for i in range(n):
    str1 = raw_input()
    str2 = raw_input()
    flag = 0
    for s in str2:
        if s in str1:
            break
        flag = 1
    if flag == 1:
        print 2+ len(str2) + 2

    for index in range(len(str2)):
        print str2[0: 1]
        if str2[0: index+1] in str1:
            print 2+ 2+ len(str2)-(index+1)+2


