#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 跳跃游戏

__author__ = 'zhangchengliang'

n = int(input())
arr = list(map(int, input().split()))

point = n-1

for i in range(n-2, -1, -1):
    if i + arr[i] >= point:
        point = i

if point == 0:
    print("true")
else:
    print("false")