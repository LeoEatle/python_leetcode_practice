class Node:
    def __init__(self, val):
        self.val = val
        self.nextlist = []

def findHeight(nodelist, count):
    for node in nodelist:
        print node
        if len(node.nextlist) == 0:
            return count
        else:
            count+=1
            return findHeight(node.nextlist, count)

while 1:
    s = raw_input()
    if s != "":
        n = int(s)
        nodelist = []
        for i in xrange(n-1):
            input = raw_input()
            a, b = input.split(" ")
            a = int(a)
            b = int(b)
            flag = 0
            for node in nodelist:
                if node.val == a:
                    b = Node(b)
                    node.nextlist.append(b)
                    flag = 1
            if flag == 0:
                a = Node(a)
                a.nextlist.append(b)
                nodelist.append(a)
            flag = 0
            print nodelist
        for node in nodelist:
            print node.val
        count = findHeight(nodelist, 1)
        print count
    else:
        break
