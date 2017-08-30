#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#description:
__author__ = 'zhangchengliang'

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

n = int(input())

arr = [(i,j) for i in range(n+1) for j in range(1, n+1) if gcd(i, j) == 1 if i <= j ]
arr = sorted(arr, key=lambda ele : float(ele[0] / ele[1]))
for ele in arr:
    print("{0}/{1}".format(ele[0], ele[1]))