(vanilla-universe)=
# Vanilla universe

To request a job in the vanilla universe, create a file `example.ini`,

```{literalinclude} 2-classad-vanilla/example.ini
:language: ini
```

And then submit your job using

```bash
condor_submit example.ini
```

After waiting for a while as the job finished, you can see what happened by reading the contents of `log`, `output`, and `error` as specified in the ClassAd.

See [](#monitor) to see how to monitor the status of your job. For advance use, use this command instead,

```bash
condor_submit example.ini; tail -F hello_world.log hello_world.out hello_world.err
```

and see [](#tail) for an explanation on what it does.

:::{note}
You'd see that output files are automatically transferred back to your submit node. We will soon see how to specify manually what to transfer, which is especially important if you have some output files under some directories.
:::

## Explanation

`executable = /bin/echo`
: **Purpose**: Defines the program or script to be executed.
: **Explanation**: The job will run the `echo` command, which is typically located in the `/bin/` directory.

`arguments = "hello world"`
: **Purpose**: Provides the arguments to be passed to the `executable`.
: **Explanation**: The `echo` command will be invoked with the argument "hello world", causing it to print this string.

`output = hello_world.out`
: **Purpose**: Specifies the file to capture the standard output of the job.
: **Explanation**: Any output produced by the `echo` command (in this case, "hello world") will be written to a file named `hello_world.out` in the job's submission directory.

`error = hello_world.err`
: **Purpose**: Specifies the file to capture the standard error of the job.
: **Explanation**: If the `echo` command produces any error messages, they will be written to this file. For this simple example, it's unlikely there will be any errors.

`log = hello_world.log`
: **Purpose**: Designates the file where HTCondor will write log messages related to the job's execution.
: **Explanation**: This file will contain logs about the job's lifecycle, such as when it was started, if it was evicted, and when it completed.

`stream_output = True`
: **Purpose**: Determines if the standard output should be streamed to the output file in real-time.
: **Explanation**: By setting this to `True`, the `hello_world.out` file will be updated in real-time as the job produces output. This can be useful for monitoring long-running jobs.

`stream_error = True`
: **Purpose**: Determines if the standard error should be streamed to the error file in real-time.
: **Explanation**: Similar to `stream_output`, this ensures that the `hello_world.err` file is updated in real-time if the job produces any error messages.

`queue`
: **Purpose**: This command tells HTCondor to add the job to its queue.
: **Explanation**: Once this ClassAd is submitted using the `condor_submit` command, HTCondor will schedule the job to run on a suitable machine in its pool.
