# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:22:18 2024

@author: kieu0
"""

ngay = int(input("Nhập ngày sinh: "))
thang = int(input("Nhập tháng sinh: "))
nam = int(input("Nhập năm sinh: "))
ngay_thang_nam = f"{ngay}/{thang}/{str(nam)[-2:]}"
print("Ngày tháng năm sinh của bạn là: ", ngay_thang_nam)