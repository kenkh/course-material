# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 23:11:57 2014

@author: Ken N
"""
s = "abcdefghijklnmopqrstuvwxyz"
r = ''
for i in range(1, len(s)+1):
    l = s[-i]
    if l in ['a', 'e', 'i', 'o', 'u']:
        l = l.capitalize()
    r = r + l
print(r)
