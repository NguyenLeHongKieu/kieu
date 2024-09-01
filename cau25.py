# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:49:14 2024

@author: kieu0
"""

chu = input("Nhập 1 chữ cái: ")
if chu.islower():
    chu_moi = chu.upper()
else:
    chu_moi = chu.lower()
print("Kết quả là: ", chu_moi)