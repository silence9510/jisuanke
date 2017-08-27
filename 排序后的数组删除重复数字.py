#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'zhangchengliang'

n = int(input())
arr = list(map(int, input().split()))
arrSet = set(arr)
sum = 0

for i in arrSet:
    if(arr.count(i) > 2):
        sum += 2
        continue
    sum += arr.count(i)

print(sum)