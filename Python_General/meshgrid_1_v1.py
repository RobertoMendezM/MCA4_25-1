# -*- coding: utf-8 -*-
"""
Meshgrid 1

Referencias:
   * A Course in Python 2023 Hazrat pag 205
   * How to Plot a Direction Field with Python Odubanjo
   link web: https://pubhtml5.com/enyy/ikvo/basic/

Created on Tue Sep  3 00:26:49 2024

@author: Roberto Méndez Méndez
"""

import numpy as np

nx, ny = (3, 2)

x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)

print(x)
print(y)

#  Meshgrid
xv, yv = np.meshgrid(x, y)

print(xv)
print(yv)