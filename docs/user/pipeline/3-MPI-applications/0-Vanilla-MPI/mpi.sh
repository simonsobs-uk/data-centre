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

# note that as you're not using the MPI wrapper script to launch in the parallel universe,
# you need to set these environment variables for the hybrid MPI parallelization to not be over-subscribed.
# rule of thumb is *_NUM_THREADS * no. of MPI processes should equals to the no. of physical (not logical) cores
# i.e. 2 threads * 4 processes = 8 physical cores here
export OPENBLAS_NUM_THREADS=2
export JULIA_NUM_THREADS=2
export TF_NUM_THREADS=2
export MKL_NUM_THREADS=2
export NUMEXPR_NUM_THREADS=2
export OMP_NUM_THREADS=2

print_double_line
echo "$(date) activate environment..."
. "$CONDA_PREFIX/bin/activate"
print_line
echo "Python is available at:"
which python
echo "mpirun is available at:"
which mpirun

print_double_line
echo 'Running TOAST tests in /tmp...'
cd /tmp
mpirun -n 4 python -c 'import toast.tests; toast.tests.run()'
