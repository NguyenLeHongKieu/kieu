# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:33:04 2024

@author: kieu0
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
d = int(input("Nhập số d: "))
if a <= b and a <= c and a <= d:
    So_be_nhat = a
elif b <= a and b <= c and b <= d:
    So_be_nhat = b
elif c <= a and c <= b and c <= d:
    So_be_nhat = c
else:
    So_be_nhat = d
print("Só bé nhất là: ", So_be_nhat)