# madelung.py: compute the Madelung constant for sodium chloride
import numpy as np
from numba import jit

@jit(nopython=True) # Set "nopython" mode for best performance, equivalent to @njit
def madelung_constant(L):
    """
    Calculates the Madelung constant for a crystal using Ewald's method.

    Returns:
    float: The Madelung constant.
    """
    M = 0.0
    for i in range(-L, L + 1):
        for j in range(-L, L + 1):
            for k in range(-L, L + 1):
                if i == j == k == 0:
                    continue
                M += (-1)**(i+j+k) / np.sqrt( i*i + j*j + k*k )
    return M
print(madelung_constant(2000))