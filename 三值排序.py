#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# description: 先把1放好，2、3调换下就好。
# 解题思路：把对方阵营自己的棋子和自己阵营对方的棋子相互交换，每次至少一步，不妨设为x次；
# 第三方阵营有自己的棋子，自己的阵营有第二方的棋子，第二方阵营有第三方的棋子，至少需要两步得以交换，
# 不妨设为y次。 故最少的排序的步数为x+y/3*2
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