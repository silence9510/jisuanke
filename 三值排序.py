#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# description: 先把1放好，2、3调换下就好。
__author__ = 'zhangchengliang'

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

c1 = arr.count(1)
c2 = arr.count(2)
c3 = arr.count(3)
num = (c1 - arr[0:c1].count(1)) + max(arr[c1:c1+c2].count(3), (arr[-c3:].count(2)))
print(num)