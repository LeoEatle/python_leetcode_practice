#!/usr/bin/env python
# coding:utf-8
# from pythonds.basic.stack import Stack

def infixToPostfix(infixexpr):
    prec = {}

    prec["*"] = 3

    prec["/"] = 3

    prec["+"] = 2

    prec["-"] = 2

    prec["("] = 1

    prec["="] = 0

    opStack = []

    postfixList = []

    tokenList = list(infixexpr)

    for token in tokenList:

        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" or token in "0123456789":

            postfixList.append(token)

        elif token == '(':

            opStack.append(token)

        elif token == ')':
            #opStack.pop()
            while opStack[-1] != '(':
                postfixList.append(opStack[-1])
                opStack.pop()
            opStack.pop()

        else:

            while (not len(opStack) == 0) and (prec[opStack[-1]] >= prec[token]):
                postfixList.append(opStack[-1])
                opStack.pop()

            opStack.append(token)

    while not len(opStack) == 0:
        postfixList.append(opStack[-1])
        opStack.pop()

    return "".join(postfixList)


s = raw_input()
if s == "":
    print ""

print(infixToPostfix(s))

# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))