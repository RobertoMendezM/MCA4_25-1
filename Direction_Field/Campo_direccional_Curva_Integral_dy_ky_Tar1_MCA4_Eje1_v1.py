# -*- coding: utf-8 -*-
"""
Directional Field 2D normalizado y Curvas Integrales

Curso:  MCA 4 2025-1 

Tema:  Ejercicio 1, Tarea 1 Arvizu

Referencias:
  * How to Plot a Direction Field with Python, Odubanjo Sec 6
     link web: https://pubhtml5.com/enyy/ikvo/basic/
  * web https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html 
  * Youtube: https://www.youtube.com/watch?v=Zobtt87M4G8
    
    
Editado  Sep 4 2024  v1

@author: Roberto Méndez Méndez
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


k = 50


# Definicónde la Derivada
def f(x,y):
    return 50*y 

#  nx, ny = .3, .3
nx, ny = .2, .2
x = np.arange(-2, 2.3, nx)
y = np.arange(-1, 1.3, ny)

# MESHGRID
X, Y = np.meshgrid(x, y)

# Derivative
dy = f(X,Y)
dx =np.ones(X.shape)

# Normalización
dyu = dy/np.sqrt(dx**2 + dy**2)
dxu = dx/np.sqrt(dx**2 + dy**2)

# Solución con odeint
y0 = -.01
steps = 10
t1 = np.linspace(-1,-.905, steps)
sol1 = odeint(f, y0, t1, tfirst=True)
y0 = .01
t2 = np.linspace(1,1.095, steps)
sol2 = odeint(f, y0, t2, tfirst=True)

# Gráfica Directional Field
plt.quiver(X,Y,dxu,dyu, color = "orange",  headwidth = 2)

# Grafica Curvas Integrales
plt.plot(t1, sol1, color='red')
plt.plot(t2, sol2, color='cyan')

plt.xticks(x, rotation = 60)
plt.yticks(y)
plt.title("Directional Field y' = 50y", color='blue', fontsize ='x-large')
plt.show()

