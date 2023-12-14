# MPI with a single node

Technically, HTCondor talks about machines rather than nodes, where a requested machine with a certain amount of CPU can be sharing the same physical node with other jobs.

In this example, we'd mention that you can run MPI applications using the vanilla universe in a single node. This is the simplest case as they do not need to communicate over multiple machines/nodes/HTCondor processes.

In `mpi.ini`,

```{literalinclude} 0-Vanilla-MPI/mpi.ini
:language: ini
```

In `mpi.sh`,

```{literalinclude} 0-Vanilla-MPI/mpi.sh
:language: sh
```

It is this simple.

:::{note}
We uses an environment from CVMFS here, where we will provide more details in [](#OpenMPI-CVMFS).

We also uses MPICH in this case. Currently we only support Open MPI with the Parallel Universe. But in the Vanilla Universe, there's no such limitation as single node MPI is really that simple.
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
