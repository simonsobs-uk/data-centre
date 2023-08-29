# Parallel universe

To request a job in the parallel universe, create a file `example.ini`,

```{literalinclude} 3-classad-parallel/example.ini
:language: ini
```

And then submit your job using

```bash
condor_submit example.ini
```

After waiting for a while as the job finished, you can see what happened by reading the contents of `log`, `output`, and `error` as specified in the ClassAd.

See [](#monitor) to see how to monitor the status of your job. For advance use, use this command instead,

```bash
condor_submit example.ini; tail -F hello_world.log hello_world-0.out hello_world-0.err hello_world-1.out hello_world-1.err
```

and see [](#tail) for an explanation on what it does.

## Explanation

universe = parallel
: This specifies that the job you're submitting is a parallel job. In HTCondor, the `universe` attribute defines the type of environment or execution context for the job. In the case of the `parallel` universe, it allows for the coordination of multiple job processes that will run simultaneously.

machine_count = 2
: This indicates that the job requires two machines (or slots) from the HTCondor pool. Essentially, the job is requesting two instances of itself to run concurrently.

request_cpus = 2
: This asks for two CPUs for each instance (or slot) of the job. So, for the two machines specified by `machine_count`, each machine should have at least 2 CPUs.

request_memory = 1024M
: This is a request for each machine (or slot) to have at least 1024 Megabytes (1 Gigabyte) of memory.

request_disk = 10240K
: This requests that each machine (or slot) has at least 10240 Kilobytes (10 Megabytes) of available disk space.

executable = /bin/echo
: This specifies the executable that will be run. In this case, it's the `echo` command commonly found on UNIX-like systems.

arguments = "hello world from process $(Node)"
: Here, the `arguments` attribute specifies what arguments will be passed to the `echo` command. The `$(Node)` is a placeholder that gets replaced with the node (or process) number when the job runs. So, for a parallel job running two instances, you'd see one instance printing "hello world from process 0" and the other "hello world from process 1".

output = hello_world-$(Node).out
: This specifies where the standard output of each job process should be written. Using the `$(Node)` placeholder, each process will write its output to a unique file. For instance, "hello_world-0.out" for the first process, "hello_world-1.out" for the second, and so on.

error = hello_world-$(Node).err
: Similarly, this defines where the standard error of each job process should be written. For instance, any errors from the first process would go to "hello_world-0.err", from the second to "hello_world-1.err", and so on.

log = hello_world.log
: This is a consolidated log file for the job. It will contain logging information from all instances of the job, such as when each instance starts, stops, etc.

stream_output = True
: This means that the standard output of the job will be streamed (written in real-time) to the specified output file, rather than being buffered and written at the end of the job.

stream_error = True
: Similarly, this streams the standard error of the job to the specified error file in real-time.

queue
: This final command actually submits the job (or jobs, if more than one) to the HTCondor scheduler. It tells HTCondor that the job is ready to be matched with available resources in the pool.
