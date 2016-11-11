def find_all(string, i):
    if i == len(string)-1:
        print "".join(string)
        return
    else:
        for j in range(i, len(string)):
            string[i],string[j] = string[j],string[i]
            find_all(string, i+1)
            string[i], string[j] = string[j], string[i]


while 1:
    s = raw_input()
    if s == '':
       break
    s = list(s)
    find_all(s, 0)
    # for i in range(len(s)):
    #     for j in range(i+1, len(s)):
    #         s[i], s[j] = s[j], s[i]
    #         print ("".join(s))
    #         s[i], s[j] = s[j], s[i]

