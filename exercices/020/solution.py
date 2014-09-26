# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 23:11:57 2014

@author: Ken N
"""
import sys

if len(sys.argv) != 3:
    print("usage: python3 " + sys.argv[0] + " OP1 OP2")
else:
    print(int(sys.argv[1]) - int(sys.argv[2]))
