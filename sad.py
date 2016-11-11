#!/usr/bin/env python
# coding=utf-8

cnt = int(raw_input())
result = []
while cnt:
    A = raw_input()
    B = raw_input()

    if A[len(A) - 1] == B[0]:
        ret = 4 + len(B) - 1
    else:
        ret = 4 + len(B)
    result.append(ret)
    cnt -= 1
for x in result:
    print x
