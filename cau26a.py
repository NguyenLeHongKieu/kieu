# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:10:18 2024

@author: kieu0
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
if a>b:
    a, b = b, a
if b>c:
    b, c = c, b
    if a>b:
        a, b = b, a
print("Tăng dàn là: ", a, b, c)