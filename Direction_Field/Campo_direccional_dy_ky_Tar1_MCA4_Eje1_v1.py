# -*- coding: utf-8 -*-
"""
Directional Field 2D normalizado

Curso:  MCA 4 2025-1 

Tema:  Ejercicio 1, Tarea 1 Arvizu

Referencias:
  * How to Plot a Direction Field with Python, Odubanjo Sec 6
     link web: https://pubhtml5.com/enyy/ikvo/basic/
  * web https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html 
    
    
Editado  Sep 4 2024  v1

@author: Roberto Méndez Méndez
"""

import numpy as np
import matplotlib.pyplot as plt


k = 50

# Definicónde la Derivada
def f(x,y):
    return k*y 


nx, ny = .3, .3
x = np.arange(-2, 2.3, nx)
y = np.arange(-1, 1.3, ny)

# MESHGRID
X, Y = np.meshgrid(x, y)

# Derivative
dy = f(X,Y)
dx =np.ones(X.shape)

# Normalizar
dyu = dy/np.sqrt(dx**2 + dy**2)
dxu = dx/np.sqrt(dx**2 + dy**2)

# Gráficas
plt.quiver(X,Y,dxu,dyu, color = "orange",  headwidth = 2)
plt.xticks(x, rotation = 60)
plt.yticks(y)
plt.title("Directional Field y' = 50y", color='blue', fontsize ='x-large')
plt.show()
