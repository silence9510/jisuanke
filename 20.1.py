#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#数字跳跃2-贪心实现
# 每次都在所能走的范围内，寻找一个最远的位置，竭力走更远；

__author__ = 'zhangchengliang'

def jump(arr, n):
    if n < 2:
        return 0;
    cur = 0
    count = 1
    while True:
        if cur + arr[cur] >= n-1:
            return count
        max = cur+1
        for i in range(cur+2, cur+arr[cur]+1):
            if i+arr[i] > max+arr[max]:
                max = i
        cur = max
        count+=1

n = int(input())
arr = list(map(int, input().split()))
print(jump(arr, n))