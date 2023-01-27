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

# Loading in the initial data 
# to numpy array
data = np.loadtxt("DOSCAR.dat")

# Separating for pltting
E = data[:, 0]
k = data[:, 1]
#print(data[:, 0])

# Finding band gap energy E_g
values_to_separate = []

for index, row in enumerate(data):
    if row[1] == 0 and 5.0 <= row[0] <= 6.5:
        values_to_separate.append((index, row[0]))

# Printing E_g values with indexes
print("-------------------------------------------",
      "\nPrinting out at which E values the band gap",
      "\noccurs in the DOSCAR.dat file:",
      "\n-------------------------------------------")
for index, value in values_to_separate:
    print("Index:", index+1, "Value:", value)

# Calculating difference of the band gap width
difference = abs(values_to_separate[0][1] - 
               values_to_separate[len(values_to_separate[:])-1][1])
print("\n E_g difference: %.4f eV\n" % np.round(difference,4) )

# Plotting
plt.plot(E, k)
plt.title("Conducting and Valence Zones")
plt.grid()
plt.show()
