import math as m
import numpy as np
from numba import jit

@jit(nopython=True) # Set "nopython" mode for best performance, equivalent to @njit
def mad_const(L):
    e = 1.602e-19 #Coloumbs
    epsNaught = 8.85e-12 #F/m
    M = 0 #Madelung constant, total potential felt by origin sodium atom
    n = 0 #Number of atoms
    for i in range(-L,L+1):
        for j in range(-L,L+1):
            for k in range(-L,L+1):
                n += 1
                distance = np.sqrt(i**2 + j**2 + k**2)

                if (i == j == k == 0): #Case for soidium atom at origin
                    continue

                potential = e / (4 * np.pi * epsNaught * distance)

                if (i+j+k)%2 == 1: #Odd, chlorine atoms, attraction = neg potential
                    potential *= -1

                M += potential

    return M

print(mad_const(100))