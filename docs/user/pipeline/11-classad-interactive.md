# Writing ClassAd—Interactive job

To request an interactive job in the vanilla universe, create a file `example.ini`,

```{literalinclude} 11-classad-interactive/example.ini
:language: ini
```

And then submit your job using

```bash
condor_submit -i example.ini
```

After submitting and waiting for a while, you will be dropped into an interactive bash shell on an interactive worker node.

:::{note}
Interactive node is in the vanilla universe in HTCondor, meaning that you cannot requests multiple nodes here.
:::

## Explanation

`RequestMemory=32999`
: This line specifies that the job requires 32,999 megabytes (or roughly 32.999 gigabytes) of memory. The HTCondor system will attempt to match this job with a machine that has at least this much available memory.

`RequestCpus=16`
: This line indicates that the job needs 16 CPUs (or cores). Again, HTCondor will try to find a machine that can provide this number of CPUs for the job.

   :::{warning}
    By default, these are number of logical cores. Because of Simultaneous multithreading (SMT), this usually means the no. of physical cores is half of this number. This will have important consequence on over-subscription that we will mention later.
    :::

`queue`
: This line is a command that tells HTCondor to queue the job. When you submit this ClassAd, the job will be added to the queue and HTCondor will try to find a suitable machine that meets the specified requirements.
