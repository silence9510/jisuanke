#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#1,11,21,1211,
#后一个是对前一个数字的解释，1个1、2个1...

__author__ = 'zhangchengliang'

def earlSeq(n):
    length = len(n)
    next = []
    now = 0
    for i in range(1, length):
        if n[i] != n[now]:
            next.append(i - now)
            next.append(n[now])
            now = i
    next.append(length - now)
    next.append(n[now])
    return next

while 1:
    n = int(input())
    m = [1]
    for i in range(n-1):
        m = earlSeq(m)
    for i in m:
        print(i, end='')
    print()