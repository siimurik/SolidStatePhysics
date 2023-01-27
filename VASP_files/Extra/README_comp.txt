These files contain more complicated paramaters for Silicon.
-------------------------------------------------------------------------------------------
KPOINTS
A KPOINTS file that uses a non-uniform k-point grid and specifies the k-point weights.

This KPOINTS file indicates that the k-point sampling should use a non-uniform grid (the 
first line), that the reciprocal lattice should be shifted (the second line), and that the 
k-point sampling should use a grid of 4x4x4 points in the reciprocal space (the third line). 
The next 15 lines specify the positions and weights of the k-points on the grid. In this 
example, the grid includes points at the corners of the Brillouin zone (the first 8 lines), 
the middle of the faces of the Brillouin zone (the next 6 lines), and the center of the 
Brillouin zone (the final line).
-------------------------------------------------------------------------------------------
INCAR
A more complicated INCAR file that could be used with the KPOINTS file from the previous 
example:

This INCAR file sets the name of the system to "Si", indicates that this is a continuation of 
a previous calculation (ISTART = 1), specifies that the charge density should be read from 
the previous CHGCAR file (ICHARG = 1), sets the energy cutoff for the plane-wave basis 
set to 520 eV (ENCUT = 520), sets the convergence criteria for the electronic self-consistent 
field to 1E-6 eV (EDIFF = 1E-6), indicates that the electronic occupations should be treated 
using the Methfessel-Paxton method with a smearing width of 0.05 eV (ISMEAR = -5 and 
SIGMA = 0.05), specifies that the real-space projection should be automatically determined 
(LREAL = Auto), that the wavefunctions should be written to the WAVECAR file (LWAVE = .TRUE.),
that the charge density should not be written to the CHGCAR file (LCHARG = .FALSE.), and that 
the k-point grid should be refined using the automatic grid adjustment algorithm 
(ADDGRID = .TRUE.).
