{#1-classad-interactive}
# Interactive job

To request an interactive job in the vanilla universe, create a file `example.ini`,

```{literalinclude} 1-classad-interactive/example.ini
:language: ini
```

Here, we assume the use of the grid storage system.
Following [](#user-credentials),
you should run

```sh
voms-proxy-init --voms souk.ac.uk --valid 168:0
```

to ensure your temporary AC is valid.

And then submit your job using

```sh
condor_submit -i example.ini
```

After submitting and waiting for a while, you will be dropped into an interactive bash shell on an interactive worker node.

:::{note}
Interactive node is in the vanilla universe in HTCondor, meaning that you cannot requests multiple nodes here.
:::

:::{note}
The interactive job started in a worker node is in a blank state.
I.e. it does not see the same `HOME` as in the submit node `vm77`.
Any of the software deployment methods or data I/O mentioned earlier can be applied here,
such as the grid storage system and CVMFS.
:::

## Explanation

`RequestMemory=32999`
: This line specifies that the job requires 32,999 megabytes (or roughly 32.999 gigabytes) of memory. The HTCondor system will attempt to match this job with a machine that has at least this much available memory.

`RequestCpus=16`
: This line indicates that the job needs 16 CPUs (or cores). Again, HTCondor will try to find a machine that can provide this number of CPUs for the job.

   :::{warning}
    By default, these are number of logical cores. Because of Simultaneous multithreading (SMT), this usually means the no. of physical cores is half of this number. This will have important consequence on over-subscription that we will mention later.
    :::

`use_x509userproxy = True`
: HTCondor will automatically transfer your AC in submit node to the worker node and set it up correctly such that you can access the grid storage system on this interactive worker node as well.

`queue`
: This line is a command that tells HTCondor to queue the job. When you submit this ClassAd, the job will be added to the queue and HTCondor will try to find a suitable machine that meets the specified requirements.
