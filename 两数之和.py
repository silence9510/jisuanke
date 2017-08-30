#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'zhangchengliang'

n = int(input())
arr = list(map(int, input().split()))
sum = int(input())

for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == sum:
            print('{0} {1}'.format(i+1, j+1))
            break
    else:
        continue
    break

