# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:54:43 2024

@author: kieu0
"""

gio = int(input("Nhập giờ: ")) 
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
tong_giay = gio*3600+phut*60+giay
print("Tổng giây là: ", tong_giay)