# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:59:52 2024

@author: kieu0
"""

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
A = ((a+b)/(a**(1/3)+b**(1/3))-(a*b)**(1/3))/(a**(1/3)-b**(1/3))*(a**(1/3)-b**(1/3))
print("Kết quả là: ", A)