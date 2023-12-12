# CVMFS

According to [CernVM-FS documentation](https://cvmfs.readthedocs.io/en/stable/),

> CernVM-FS is implemented as a POSIX read-only file system in user space (a FUSE module). Files and directories are hosted on standard web servers and mounted in the universal namespace `/cvmfs`.

The key here is that it is read-only, suitable for software deployment.
While there is a caching mechanism,
it means that it has high latency on first launch on a node that has never fetch this software before.

We will see how it works in the following example.

## Example

create a file `cvmfs.ini`,

```{literalinclude} 2-CVMFS/cvmfs.ini
:language: ini
```

The ClassAd involve a script `cvmfs.sh`,

```{literalinclude} 1-cvmfs/cvmfs.sh
:language: sh
```

Here, we see that `CVMFS='/cvmfs/...'` is defined.
The example path given here is a minimal conda environment.

In this script,
the environment is first activated,
and then it shows you the environment is loaded successfully,
as evident by seeing which Python it is loading.

As usual, you can submit the job via

```sh
condor_submit cvmfs.ini
```

See [](#monitor-your-jobs) to see how to monitor the status of your job. For advance use, use this command instead,

```sh
condor_submit cvmfs.ini; tail -F cvmfs.log cvmfs.out cvmfs.err
```

and see [](#tail) for an explanation on what it does.
