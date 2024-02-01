"""
Programa que suma dos vectores 
y muestra que la suma es conmutativa


editor: Roberto Méndez

Libro: Linear Algebra with Python 2023 Tsukada Kobayashi

date: 31 Jan 24

"""

from numpy import array
import matplotlib.pyplot as plt

# o Origen
# x vector x
# x vector x

o, x, y = array([0, 0]), array([3, 2]), array([1, 3])


arrows = [(o, x + y, 'b'), (o, x, 'r'), (x, y, 'g'),
          (o, y, 'g'), (y, x, 'r')]


#                 PLOT

# p initial vector (point)
# v end vector 
# c color 

for p, v, c in arrows:
    plt.quiver(p[0], p[1], v[0], v[1],
               color=c, units='xy', scale=1)

# Atributes

plt.axis('scaled'), plt.xlim(0, 5), plt.ylim(0, 5)

# to show the graphic

plt.show()
