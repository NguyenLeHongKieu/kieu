# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:42:13 2024

@author: kieu0
"""

so = int(input("Nhập 1 số nguyên: "))
so_nguyen = {0: "Khong", 1: "Mot", 2: "Hai", 3: "Ba", 4: "Bon", 5: "Nam", 6: "Sau", 7: "Bay", 8: "Tam", 9:"Chin"}
if so in so_nguyen:
    print(so_nguyen[so])
else:
    print("Khong doc duoc")