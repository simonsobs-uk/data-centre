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
echo "Unpacking environment..."
tar -xzf pmpm-20230718-Linux-x86_64-OpenMPI.tar.gz -C /tmp
. /tmp/pmpm-20230718/bin/activate /tmp/pmpm-20230718
print_line
echo "Environment is available at:"
which python
which mpirun

print_double_line
echo "Running TOAST tests..."
python -c "import toast.tests; toast.tests.run()"
