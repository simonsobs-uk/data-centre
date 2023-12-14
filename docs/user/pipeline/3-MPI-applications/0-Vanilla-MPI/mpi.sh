#!/usr/bin/env bash

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

CONDA_PREFIX=/cvmfs/northgrid.gridpp.ac.uk/simonsobservatory/pmpm/so-pmpm-py310-mkl-x86-64-v3-mpich-latest

print_double_line
echo "$(date) activate environment..."
. "$CONDA_PREFIX/bin/activate" "$CONDA_PREFIX"
print_line
echo "Python is available at:"
which python
echo "mpirun is available at:"
which mpirun

print_double_line
echo 'Running TOAST tests in /tmp...'
cd /tmp
mpirun -n 8 python -c 'import toast.tests; toast.tests.run()'
