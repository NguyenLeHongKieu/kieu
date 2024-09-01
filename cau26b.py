# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:54:52 2024

@author: kieu0
"""

N = input("Nhập 1 số nguyên N: ")
so = list(N)
so.sort()
so_tang_dan = ''.join(so)
print("Tăng dần là: ", so_tang_dan)