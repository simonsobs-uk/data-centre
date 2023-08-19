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

print_double_line
set_OMPI_HOST_one_slot_per_condor_proc
echo "Running mpirun with host configuration: $OMPI_HOST" >&2

print_double_line
echo "Running TOAST tests..."
mpirun -v -host "$OMPI_HOST" python -c 'import toast.tests; toast.tests.run()'
