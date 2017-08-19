#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#跳跃游戏2

# 逐步逼近终点；
# H[i]表示从0到i的最少跳数，若H[i]=m，则去更新(i, i+m]这个区间的最少跳数；
# 这个区间的跳数，都可以选择用H[i]+1，但是可能存在更好的选择，因此每次都比较下，取最小的跳数；

__author__ = 'zhangchengliang'

def jump(arr, n):
    if n < 2:
        return 0

    H = []
    for i in range(n):
        H.append(0)

    for i in range(n-1):
        m = arr[i]
        if i+m >= n-1:
            return H[i]+1
        for j in range(1, m+1):
            if H[i+j] == 0 or H[i+j] > H[i]+1:
                H[i+j] = H[i] + 1
    return H[n-1]

n = int(input())
arr = list(map(int, input().split()))
print(jump(arr, n))