# coding=utf-8
def bag(n, c, w, v):
    res = [[-1 for j in range(c + 1)] for i in range(n + 1)]
    for j in range(c + 1):
        res[0][j] = 0
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            res[i][j] = res[i - 1][j]
            if j >= w[i - 1] and res[i][j] < res[i - 1][j - w[i - 1]] + v[i - 1]:
                res[i][j] = res[i - 1][j - w[i - 1]] + v[i - 1]
    return res

user = raw_input().split(" ")
n = int(user[1])
c = int(user[0])
w = []
v = []
for i in range(n):
    card = raw_input().split(" ")
    w.append(int(card[0]))
    v.append(int(card[1]))
res = bag(n, c, w, v)
print(res[n][c])