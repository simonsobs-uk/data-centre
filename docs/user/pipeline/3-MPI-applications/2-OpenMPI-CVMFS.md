{#OpenMPI}
# OpenMPI with CVMFS

This is similar to the previous example but with CVMFS instead.
 
## Deploying MPI applications using the provided wrapper

Create a file `mpi.ini`:

```{literalinclude} 2-OpenMPI-CVMFS/mpi.ini
:language: ini
```

Note that it calls a wrapper script `cbatch_openmpi`.

Note that this script takes 2 arguments, both are also scripts, where the 1st one setup the software environment and the second one runs the MPI application.

In the first file `env.sh`,

```{literalinclude} 2-OpenMPI-CVMFS/env.sh
:language: sh
```

We see that it is basically preparing for the software environment following [](#cvmfs-simple).

The reason this wrapper script has such an interface is because MPI is part of your software environment. Only after you loaded this environment (where you can change to any OpenMPI installation you want as long as it is OpenMPI), the wrapper script can continue to start the OpenMPI launcher to prepare for you to run `mpirun` later.

Then in `mpi.sh`,

```{literalinclude} 2-OpenMPI-CVMFS/mpi.sh
:language: sh
```

Here `set_OMPI_HOST_one_slot_per_condor_proc`, provided within the wrapper script, is called to set `OMPI_HOST`. There are 2 such bash functions provided. Be sure to read the `cbatch_openmpi` documentation to know which one to choose. The recommended setup for Hybrid MPI such as MPI+OpenMP is to use `set_OMPI_HOST_one_slot_per_condor_proc` such that each HTCondor process is one MPI process.

Note the use of `mpirun -host "$OMPI_HOST" ...`, which uses the prepared `OMPI_HOST` to launch the MPI processes.

:::{warning}
When writing these scripts such as `env.sh` and `mpi.sh`, note that in parallel universe in HTCondor, the `executable` is run in the single program, multiple data (SPMD) paradigm. This is very different from what you would do in SLURM's batch script for example.

As a concrete example, if there's a line `echo hello world` in your scripts, in each HTCondor process, `echo hello world` will be run once, and there corresponding `mpi-?.out` files will each have a `hello world` there.

So when `env.sh` is run, in each of the HTCondor process, the software environment is being preparing individually. This is important, as all processes should shares exactly the same software environment to launch an MPI program.
:::

Lastly, submit the job as usual by

```sh
condor_submit mpi.ini
```

After waiting for a while as the job finished, you can see what happened by reading the contents of `log`, `output`, and `error` as specified in the ClassAd.

See [](#monitor-your-jobs) to see how to monitor the status of your job. For advance use, use this command instead,

```sh
condor_submit mpi.ini; tail -F mpi.log mpi-0.out mpi-0.err mpi-1.out mpi-1.err
```

and see [](#tail) for an explanation on what it does.

:::{warning}
It is known that when running the TOAST3 test suite with OpenMPI using our provided software environment has some failed unit tests. We are investigating and will be fixed in the future.
:::
