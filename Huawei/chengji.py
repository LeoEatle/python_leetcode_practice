# coding: utf-8

n = raw_input()
subjects = []
for i in n.split(" "):
    num = int(i)
    subjects.append(num)
result = None
for i in subjects:
    if i < 0 or i > 150:
        continue
    if result == None or i > result:
        result = i
print subjects.index(result)+1

