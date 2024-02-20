# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 17:52:42 2024

@author: Roberto Méndez

Topic: Direction Fields

Adaptación de: 
https://matplotlib.org/stable/gallery/images_contours_and_fields/quiver_
       demo.html#sphx-glr-gallery-images-contours-and-fields-quiver-demo-py
"""

import matplotlib.pyplot as plt
import numpy as np

# EXAMPLE 1
 
X, Y = np.meshgrid(np.arange(-3, 3, .2), np.arange(-3, 3, .2))
dxdt = -Y
dydt = X

fig1, ax1 = plt.subplots()
ax1.set_title('Direction Field')
Q = ax1.quiver(X, Y, dxdt, dydt, units='x')
#qk = ax1.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
 #                  coordinates='figure')
 
 
# EXAMPLE 2
 
X, Y = np.meshgrid(np.arange(-3, 3, .2), np.arange(-3, 3, .2))
dxdt = X
dydt = X**2

fig2, ax2 = plt.subplots()
ax2.set_title('Direction Field')
Q = ax2.quiver(X, Y, dxdt, dydt, units='x')


#EXAMPLE 3
X, Y = np.meshgrid(np.arange(-2.5, 2.5, .3), np.arange(-2.5, 2.5, .3))
dxdt = 1
dydt = Y*X**2

fig3, ax3 = plt.subplots()
ax3.set_title('Direction Field')
Q = ax3.quiver(X, Y, dxdt, dydt, units='x')

#EXAMPLE 4
X, Y = np.meshgrid(np.arange(-3, 3, .2), np.arange(-2, 1, .2))
dxdt = 1
dydt = 3*Y + 2

fig4, ax4 = plt.subplots()
ax4.set_title('Direction Field')
Q = ax4.quiver(X, Y, dxdt, dydt, units='x')