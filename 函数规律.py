#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#数圈圈
__author__ = 'zhangchengliang'

def oo(n):
    dict = {0:1, 6:1, 8:2, 9:1}
    return dict[0]*n.count('0') + dict[6]*n.count('6') + dict[8]*n.count('8') + dict[9]*n.count('9')

# n = list(map(int, input().split()))
n = str(input())
print(oo(n))