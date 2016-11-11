#coding=utf-8
while 1:
    s = raw_input()
    if s != "":
        result = 1
        count = 2
        while count <= int(s):
            if (count%2 == 0):
                result = result + count/2
                count=count+1
            elif (count%2 == 1):
                result = result -1
                count= count + 1
        print result

    else:
        break