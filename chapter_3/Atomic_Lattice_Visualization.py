from vpython import *
from numpy import linspace

L = 5
R = 0.3

atoms = linspace(0, (L*2)**3)

for i in range(-L, L + 1):
    for j in range(-L, L + 1):
        for k in range(-L, L + 1):
            sphere(pos=vector(i,j,k), radius=R)
