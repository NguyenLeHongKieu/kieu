# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:36:17 2024

@author: kieu0
"""

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
if gio >= 0 and gio <24 and phut >= 0 and phut < 60 and giay >=0 and giay <60:
    print("Thời gian nhập vào hợp lệ.")
else:
    print("Thời gian nhập vào không hợp lệ.")