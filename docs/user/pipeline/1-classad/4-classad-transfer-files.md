# Transferring files

## Implicit transfer of `executable`

The simplest example that involve file transfer is the job script itself.

create a file `repl.ini`,

```{literalinclude} 4-classad-transfer-files/repl.ini
:language: ini
```

and a file `repl.sh`,

```{literalinclude} 4-classad-transfer-files/repl.sh
:language: sh
```

This ClassAd involve transferring a script named `repl.sh`, and be default it will be copied to worker nodes.

And then you can submit your job using

```sh
condor_submit repl.ini
```

After waiting for a while as the job finished, you can see what happened by reading the contents of `log`, `output`, and `error` as specified in the ClassAd.

See [](#monitor-your-jobs) to see how to monitor the status of your job. For advance use, use this command instead,

```sh
condor_submit repl.ini; tail -F repl.log repl-0.out repl-0.err repl-1.out repl-1.err
```

and see [](#tail) for an explanation on what it does.

:::{note}
We normally won't use the `module` system here, but if needed, notice the shebang `#!/bin/bash -l` is necessary for `module` to be found.
:::

This example also includes some information specific to HTCondor that you can play around.

## Explicit file transfer

Create a file `cat.ini`,

```{literalinclude} 4-classad-transfer-files-2/cat.ini
:language: ini
```

Over here, we use `transfer_input_files` to specify which input files to be copied to the worker nodes. If it is a relative path, it will be the relative path w.r.t. the current directory that you are submitting the job from.

To prepare the file for `transfer_input_files`, let's create `cat.txt` with the content,

```{literalinclude} 4-classad-transfer-files-2/cat.txt
```

And then submit your job using

```sh
condor_submit cat.ini
```

After waiting for a while as the job finished, you can see what happened by reading the contents of `log`, `output`, and `error` as specified in the ClassAd.

See [](#monitor-your-jobs) to see how to monitor the status of your job. For advance use, use this command instead,

```sh
condor_submit cat.ini; tail -F cat.log cat-0.out cat-0.err cat-1.out cat-1.err
```

and see [](#tail) for an explanation on what it does.

If you want to transfer more than one files, delimit them with a comma, like so:

```ini
transfer_input_files = file1,file2,/path/to/file3
```
