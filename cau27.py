# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:02:02 2024

@author: kieu0
"""

import math
hinh = input("Nhập hình: Hình vuông(v), Hình chữ nhật(n), Hình trong(t): ")
if hinh == "v":
    canh = float(input("Nhập chiều dài cạnh của hình vuông: "))
    chu_vi_v = canh * 4
    dien_tich_v = canh * canh
    print("Kết quả P: ", chu_vi_v)
    print("Kết quả S: ", dien_tich_v)
elif hinh == "n":
    rong = float(input("Nhập chiều rộng: "))
    dai = float(input("Nhập chiều dài: "))
    chu_vi_n = (rong+dai) * 2
    dien_tich_n = rong * dai
    print("Kết quả P: ", chu_vi_n)
    print("Kết quả S: ", dien_tich_n)
elif hinh == "t":
    ban_kinh = float(input("Nhập bán kính: "))
    chu_vi_t = 2*math.pi*ban_kinh
    dien_tich_t = math.pi*ban_kinh*ban_kinh
    print("Kết quả P: ", chu_vi_t)
    print("Kết quả S: ", dien_tich_t)
else:
    print("vui lòng nhập đúng kí tự hình được yêu cầu.")