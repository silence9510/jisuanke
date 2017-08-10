#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'zhangchengliang'

a = input()
b = input()
for i in range(len(a)):
    if(a[i] == b[i]):
        print('1',end='')
    else:
        print('0',end='')