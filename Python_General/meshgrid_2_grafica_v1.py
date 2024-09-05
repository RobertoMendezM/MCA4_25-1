# -*- coding: utf-8 -*-
"""
Meshgrid 2

Referencias:
    How to Plot a Direction Field with Python, Odubanjo Sec 4
    link web: https://pubhtml5.com/enyy/ikvo/basic/

Created on Tue Sep  3 20:16:22 2024

@author: Roberto Méndez Méndez

Python 3.12.4
"""

import numpy as np
import matplotlib.pyplot as plt


nx, ny = .3, .3
x = np.arange(-3, 3, nx)
y = np.arange(-1, 2, ny)

# MESHGRID
X, Y = np.meshgrid(x, y)


# GRÁFICA
plt.plot(X, Y, marker=".", color='b', linestyle='none')
plt.xticks(x, rotation = 60)
plt.yticks(y)
plt.title('Grid plot with points')
plt.show()