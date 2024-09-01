# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:46:34 2024

@author: kieu0
"""

N = int(input("Nhập số nguyên dương có 2 chữ số: "))
if 10<=N<=99:
    hang_chuc = N//10
    hang_don_vi = N%10
    tong_hai_chu_so = hang_chuc+hang_don_vi
    print("Tổng các chữ số của N là: ", tong_hai_chu_so)
else:
    print("Số nhập vào không phải số nguyên dương có 2 chữ số")