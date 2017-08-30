#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'zhangchengliang'

l = int(input())
max = int(input())
dSquare = []

for i in range(max+1):
    for j in range(max+1):
        dSquare.append(i*i + j*j)

dSquare = list(set(dSquare))
mdv = (max*max*2 - 0) // (l - 1)
nu = 0

for dv in range(1, mdv+1):
    for i in range(len(dSquare)):
        if dSquare[-1] >= (dSquare[i] + (l-1)*dv):
            signal = 1
            for j in range(1, l):
                if signal == 1:
                    if dSquare.count(dSquare[i] + j*dv) == 0:
                        signal = 0
            else:
                if signal == 1:
                    print('{0} {1}'.format(dSquare[i], dv))
                    nu += 1
if nu == 0:
    print("NONE")
