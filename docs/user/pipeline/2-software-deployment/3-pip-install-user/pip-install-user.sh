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

print_double_line
CONDA_PREFIX=/cvmfs/northgrid.gridpp.ac.uk/simonsobservatory/conda/so-conda-py310-20240104
. "${CONDA_PREFIX}/bin/activate"
echo "Conda environment loaded with python available at:"
which python
export PATH="/cvmfs/northgrid.gridpp.ac.uk/simonsobservatory/usr/bin:$PATH"

print_double_line
echo "Note that this package doesn't exist yet:"
python -c 'import souk; print(souk.__file__)'

print_double_line
echo 'Installing souk from pip:'
pip install --user souk

print_double_line
echo 'Note that this package now exists:'
python -c 'import souk; print(souk.__file__)'
which souk_arch_info
