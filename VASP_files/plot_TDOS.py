"""
====================================     
     Siim Erik Pugal
     214704YAFM
     January 2023
====================================    
DOSCAR.dat data:
     -7.645  0.0000E+00  0.0000E+00
     -7.566  0.0000E+00  0.0000E+00
     -7.486  0.0000E+00  0.0000E+00
     -7.406  0.0000E+00  0.0000E+00
====================================    
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("TDOS.dat")

E = data[:, 0]
#print(E[0:5])
x = data[:, 1]

plt.plot(E, x)
plt.title("Density of State")
plt.grid()
plt.show()

