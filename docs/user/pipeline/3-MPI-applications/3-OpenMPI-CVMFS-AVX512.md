{#OpenMPI-CVMFS-AVX512}
# OpenMPI with CVMFS with AVX-512 CPU instructions

This is similar to the previous example but with AVX-512 instructions instead.
Please refer to the last example for more explanations.
Below we will only show the example.
 
## Deploying MPI applications using the provided wrapper

Create a file `mpi.ini`:

```{literalinclude} 3-OpenMPI-CVMFS-AVX512/mpi.ini
:language: ini
```

In the first file `env.sh`,

```{literalinclude} 3-OpenMPI-CVMFS-AVX512/env.sh
:language: sh
```

Then in `mpi.sh`,

```{literalinclude} 3-OpenMPI-CVMFS-AVX512/mpi.sh
:language: sh
```

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
