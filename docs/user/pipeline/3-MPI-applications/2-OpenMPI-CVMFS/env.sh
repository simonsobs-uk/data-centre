#!/bin/bash -l

# helpers ##############################################################

COLUMNS=72

print_double_line() {
	eval printf %.0s= '{1..'"${COLUMNS}"\}
	echo
}

print_line() {
	eval printf %.0s- '{1..'"${COLUMNS}"\}
	echo
}

########################################################################

CONDA_PREFIX=/cvmfs/northgrid.gridpp.ac.uk/simonsobservatory/pmpm/so-pmpm-py310-mkl-x86-64-v3-openmpi-latest

print_double_line
echo "$(date) activate environment..."
source "$CONDA_PREFIX/bin/activate"
print_line
echo "Python is available at:"
which python
echo "mpirun is available at:"
which mpirun
