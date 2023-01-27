--------------------------------------------------------------------------------------------
Exam question answers are in the TKF_Exam_Pugal.pdf file.
--------------------------------------------------------------------------------------------
To see plots of Fermi and band gap energy, run the Python files with DOSCAR.dat and TDOS.dat
	$ python3 plot_DOSCAR.py	# Band gap energy plot with gap energy value
	$ python3 plot_TDOS.py		# Density of state plot
--------------------------------------------------------------------------------------------
How to log into remote desktop to use VASP:
	$ ssh -X -l sipuga 193.40.252.77
	$ {password}
--------------------------------------------------------------------------------------------
POSCAR
A POSCAR file is a text-based file that provides information about the positions of atoms 
in a crystal structure

This POSCAR file defines a simple cubic crystal structure of silicon with a lattice constant 
of 3.839 angstroms. The first line specifies the name of the element, in this case silicon. 
The next three lines define the lattice vectors for the unit cell in Cartesian coordinates, 
with the x, y, and z components listed on each line. The fourth line indicates the number 
of atoms in the unit cell, and the fifth line specifies the coordinate system used for the 
atomic positions. The final two lines give the positions of the silicon atoms in the unit 
cell, with the x, y, and z coordinates listed on each line.
------------------------------------------------------------------------------------------
INCAR
An INCAR file is a text-based file that provides input parameters for the VASP (Vienna Ab 
initio Simulation Package) software. 
Here is a brief explanation of the parameters in the VASP INCAR file:

*   System: The name of the system being simulated.
*   ISTART: Controls the starting point of the calculation. 0 means that the calculation 
starts from scratch, 1 means that the calculation continues from a previously saved WAVECAR 
file, and 2 means that the calculation continues from a previously saved CONTCAR file.
*   ICHARG: Controls the starting charge density. 0 means that the charge density is read 
from the CHGCAR file, 1 means that the charge density is read from the WAVECAR file, and 2 
means that the charge density is set to a uniform charge density.
*   IBRION: Controls the type of structural relaxation. 0 means that no structural relaxation 
is performed, 1 means that a conjugate gradient relaxation is performed, 2 means that a quasi-
Newton relaxation is performed, and 3 means that a steepest descent relaxation is performed.
*   ISIF: Controls which degrees of freedom are relaxed during a structural relaxation. 2 
means that only the cell shape is relaxed, 3 means that both the cell shape and the atom 
positions are relaxed, and 4 means that the cell shape, atom positions, and the unit cell 
origin are relaxed.
*   NSW: The maximum number of ionic steps in a structural relaxation.
*   ENCUT: The energy cutoff for the plane wave expansion.
*   EDIFF: The convergence criteria for the energy difference between ionic steps.
*  ISMEAR: Controls the type of smearing used for the electronic structure calculation. -5 
means that a Gaussian smearing is used with a width of SIGMA, 0 means that a Fermi-Dirac 
smearing is used, and 1 means that a Methfessel-Paxton smearing is used.
*   SIGMA: The width of the Gaussian smearing used for the electronic structure calculation.
*   LREAL: Controls whether the projection operators are treated in real space or reciprocal 
space. .FALSE. means that the projection operators are treated in reciprocal space, and .TRUE. 
means that the projection operators
------------------------------------------------------------------------------------------
KPOINTS
A KPOINTS file is a text-based file that provides information about the k-point sampling used 
in a VASP calculation.

This KPOINTS file indicates that the k-point sampling should be determined automatically (the 
first line), that the reciprocal lattice should be shifted (the second line), and that the 
k-point sampling should use a uniform grid of 8x8x8 points in the reciprocal space (the third 
and fourth lines). The last line specifies that the k-point grid should be centered at the 
Gamma point (the point at the center of the first Brillouin zone).
------------------------------------------------------------------------------------------
