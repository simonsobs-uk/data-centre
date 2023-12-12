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

CVMFS='/cvmfs/northgrid.gridpp.ac.uk/simonsobservatory/opt/miniforge3'

print_double_line
echo "Loading a conda environment from CVMFS: $CVMFS"
. "$CVMFS/bin/activate"
print_line
echo "Environment is available at:"
which python
