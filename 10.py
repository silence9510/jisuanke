#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#移除数组中重复元素
__author__ = 'zhangchengliang'

n = int(input())
arr = map(int, input().split())
print(len(set(arr)))