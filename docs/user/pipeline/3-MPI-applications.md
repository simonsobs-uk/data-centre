# MPI Applications

```{toctree}
:maxdepth: 2
:hidden:
:glob:

3-MPI-applications/*
```

HTCondor's parallel universe is generic, in the sense that it is not designed around MPI specifically. Unlike other workload manager such as SLURM, the MPI launcher needs to be bootstrapped in the beginning of a parallel job. Therefore, a wrapper script is provided by us to encapsulate the MPI bootstrapping process. You are welcome to modify from the provided wrapper scripts to tailor for your specific workflows.

For now, OpenMPI is supported. We are investigating in making MPICH3+ works and eventually we would probably support MPICH3+ only.
