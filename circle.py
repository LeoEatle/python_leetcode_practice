import math
while 1:
    s = raw_input()
    if s == "":
        break
    else:
        r = math.sqrt(int(s))
        floor_r = int(math.floor(r))
        count = 0
        for x in range(0, floor_r):
            y = int(s) - x*x
            if int(y) == y:
                count = count + 4
        print count
