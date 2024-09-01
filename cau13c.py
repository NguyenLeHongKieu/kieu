# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:18:46 2024

@author: kieu0
"""

ngay = int(input("Nhập ngày sinh của bạn: "))
thang = int(input("Nhập tháng sinh của bạn: "))
nam = int(input("Nhập năm sinh của bạn: "))
nam_thang_ngay = f"{nam}/{thang}/{ngay}"
print("Năm tháng ngày sinh của bạn là: ", nam_thang_ngay)