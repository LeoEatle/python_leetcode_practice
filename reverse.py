#coding: utf-8
while 1:
    a = []
    s = raw_input()
    # raw_input()里面不要有任何提示信息
    if s != "":
        l = s.split()
        l.reverse()
        result = " ".join(l)
        print result
    else:
        break