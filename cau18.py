# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:35:43 2024

@author: kieu0
"""

gio1 = int(input("Nhập giờ 1: "))
phut1 = int(input("Nhập phút 1: "))
giay1 = int(input("Nhập giây 1: "))
gio2 = int(input("Nhập giờ 2: "))
phut2 = int(input("Nhập phút 2: "))
giay2 = int(input("Nhập giây 2: "))
gio_tong = gio1 + gio2
phut_tong = phut1 + phut2
giay_tong = giay1+ giay2
gio_hieu = gio1 - gio2
phut_hieu = phut1 - phut2
giay_hieu = giay1 - giay2
print("Tổng giờ là: ", gio_tong)
print("Tổng phút là: ", phut_tong)
print("Tổng giây là: ", giay_tong)
print("Hiệu giờ là: ", gio_hieu)
print("Hiệu phút là: ", phut_hieu)
print("Hiệu giây là: ", giay_hieu)