#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'zhangchengliang'

def maxsubsum(arr, n):
    thissum, maxsum, ele = 0, 0, arr[0]

    for i in range(n):
        thissum += arr[i]
        if thissum > maxsum:
            maxsum = thissum
        if thissum < 0:
            thissum = 0
        if arr[i] > ele:
            ele = arr[i]
    if maxsum == 0:
        return ele
    else:
        return (maxsum>ele and maxsum or ele)

n = int(input())
arr = list(map(int,input().split()))
print(maxsubsum(arr, n))