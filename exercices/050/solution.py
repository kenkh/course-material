# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 23:11:57 2014

@author: Ken N
"""
s = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        s = s + i
print(s)
