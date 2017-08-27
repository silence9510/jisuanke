#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 加一

__author__ = 'zhangchengliang'

from functools import reduce

def arr2num(ar1):
    def fn(x, y):
        return x*10 + y
    return reduce(fn, arr)+1

def num2arr(num):
    arr = []
    while num != 0:
        arr.append(num % 10)
        num //= 10
    return arr

n = int(input())
arr = list(map(int, input().split()))

for i in reversed(num2arr(arr2num(arr))):
    print(i, end=" ")