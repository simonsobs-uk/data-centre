{#tail}
# Streaming stdout & stderr with tail

When submitting a job in HTCondor (and any other computing facilities), often your job will be run on another node at a later time. If you eager to look at the output (stdout & stderr) as soon as it is running, HTCondor provided a facility to do that together with some UNIX utilities.

Firstly, HTCondor has a facility to stream the stdout & stderr from the worker nodes back to the submit node you are working on. To use a specific example from [](#vanilla-universe),

```ini
...
output = hello_world.out
error = hello_world.err
log = hello_world.log
stream_output = True
stream_error = True
...
```

The `stream_output` & `stream_error` instructs the job to stream the stdout & stderr back to your submit node in real time (which would normally be transferred back only after the job terminates).

If we submit the job and run the `tail` command at once, like this

```sh
condor_submit example.ini; tail -F hello_world.log hello_world.out hello_world.err
```

Then the UNIX command `tail` would *follow* the files listed (which are the `output`, `error` and `log` specified in your ClassAd) as soon as new contents are available.

## Detailed explanations

As an example, the output would looks something like

```console
$ condor_submit example.ini; tail -F hello_world.log hello_world.out hello_world.err
Submitting job(s).
1 job(s) submitted to cluster 511.
```

which is the stdout from `condor_submit example.ini`. Then

```console
==> hello_world.log <==
```

is the tail command working immediately to follow contents of `hello_world.log`, with the following contents:

```console
000 (511.000.000) 2023-08-29 23:39:35 Job submitted from host: <195.194.109.199:9618?addrs=195.194.109.199-9618+[2001-630-22-d0ff-5054-ff-fe9a-b662]-9618&alias=vm77.tier2.hep.manchester.ac.uk&noUDP&sock=schedd_2377818_f2b3>
...
```

Then

```console
tail: cannot open ‘hello_world.out’ for reading: No such file or directory
tail: cannot open ‘hello_world.err’ for reading: No such file or directory

```

is `tail` telling us that `hello_world.out` & `hello_world.err` does not exist yet, as the job hasn't started. `tail` will follow them as soon as they are available. Then `hello_world.log` continues to have more content, indicating its progress:

```console
==> hello_world.log <==
040 (511.000.000) 2023-08-29 23:39:35 Started transferring input files
        Transferring to host: <195.194.109.209:9618?addrs=195.194.109.209-9618+[2001-630-22-d0ff-5054-ff-fee9-c3d]-9618&alias=vm75.in.tier2.hep.manchester.ac.uk&noUDP&sock=slot1_4_1883_7e66_41406>
...
040 (511.000.000) 2023-08-29 23:39:35 Finished transferring input files
...
```

Then

```console
tail: ‘hello_world.out’ has appeared;  following end of new file
tail: ‘hello_world.err’ has appeared;  following end of new file
```

tells us that these files finally appeared (as the job has started). Then

```console
001 (511.000.000) 2023-08-29 23:39:36 Job executing on host: <195.194.109.209:9618?addrs=195.194.109.209-9618+[2001-630-22-d0ff-5054-ff-fee9-c3d]-9618&alias=vm75.in.tier2.hep.manchester.ac.uk&noUDP&sock=startd_1389_5123>
...

```

continues to show more log from `hello_world.log`. This part

```console
==> hello_world.out <==
hello world


```

Is the content of `hello_world.out` as soon as it appears, where in the end it has the following log:

```console
==> hello_world.log <==
006 (511.000.000) 2023-08-29 23:39:36 Image size of job updated: 35
        0  -  MemoryUsage of job (MB)
        0  -  ResidentSetSize of job (KB)
...
005 (511.000.000) 2023-08-29 23:39:36 Job terminated.
        (1) Normal termination (return value 0)
                Usr 0 00:00:00, Sys 0 00:00:00  -  Run Remote Usage
                Usr 0 00:00:00, Sys 0 00:00:00  -  Run Local Usage
                Usr 0 00:00:00, Sys 0 00:00:00  -  Total Remote Usage
                Usr 0 00:00:00, Sys 0 00:00:00  -  Total Local Usage
        0  -  Run Bytes Sent By Job
        33088  -  Run Bytes Received By Job
        0  -  Total Bytes Sent By Job
        33088  -  Total Bytes Received By Job
        Partitionable Resources :    Usage  Request Allocated
           Cpus                 :                 1         1
           Disk (KB)            :       44       35    832179
           Memory (MB)          :        0        1       100

        Job terminated of its own accord at 2023-08-29T22:39:36Z.
...
```

You will notice that the `tail` process has never ended, as if it is halting. The reason is that you are not looking at the output of the job itself, but monitoring the streaming output from the job via `tail`. As far as `tail` is concerned, it will continue to monitor (follow) any new contents from these 3 files and print it on your screen.

From the content itself, you see `Job terminated of its own accord...` meaning that your job has ended, and you should now press `Ctrl + c` to terminate the `tail` command.

You can also checkout [](#monitor-your-jobs) to see how to monitor the status of your job, and from it you can tell this job has indeed ended.
