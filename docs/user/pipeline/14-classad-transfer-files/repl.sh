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
echo "hostname: $(hostname)"
print_line
echo "CPU:"
print_line
lscpu
echo Hello from $_CONDOR_PROCNO of $_CONDOR_NPROCS

print_double_line
echo "HTCondor config summary:"
print_line
condor_config_val -summary

print_double_line
echo "Current environment:"
print_line
env | sort

print_double_line
echo "Avaiable MPI:"
module avail mpi

module load mpi/openmpi3-x86_64

print_double_line
echo "Current environment:"
print_line
env | sort

print_double_line
echo "module path:"
which mpicc
which mpirun
