# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:41:47 2024

@author: kieu0
"""

a = int(input("Nhập biển số xe có 4 chữ số: "))
a=str(a) ; s=0 
for i in range(len(a)):
    s+=int(a[i])
print("Biển số xe có số nút là: ", s%10)