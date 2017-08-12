#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'zhangchengliang'

n = int(input())
arr0 = list(map(int, input().split()))
arr1 = set(arr0)

for a in arr1:
    if arr0.count(a) == 1:
        print(a)

"""
-------------c 位运算实现----------------
先变成二进制，每位除3，剩下的就是一次的

#include <cstdio>
#include <cstring>
int arr[32];
int main()
{
  int n, a, b, x;
  while(~scanf("%d", &n)) {
    a = b = 0;
    memset(arr, 0, sizeof(arr));
    for(int i = 0; i < n; i++) {
      scanf("%d", &x);
      for(int i = 0; i < 32; i++) {
        arr[i] = (arr[i] + (x & 1)) % 3;
        x >>= 1;
      }
    }
    b = 0;
    for(int i = 0; i < 32; i++) {
      b += arr[i] << i;
    }
    printf("%d\n", b);
  }
  return 0;
}
"""
