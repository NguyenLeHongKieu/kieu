# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:14:30 2024

@author: kieu0
"""

import math 
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
delta = b**2 - 4*a*c
if delta >0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Phương trình có 2 nghiệm phân biệt: ", x1, x2)
elif delta ==0:
    x = -b/(2*a)
    print("Phương trình có nghiệm kép: ", x)
else: 
    print("Phương trình không có nghiệm thực.")