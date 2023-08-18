# Transferring files

The simplest example that involve file transfer is the job script itself.

create a file `example.ini`,

```{literalinclude} 4-classad-transfer-files/repl.ini
:language: ini
```

This ClassAd involve transferring a script named `repl.sh`, and be default it will be copied to worker nodes:

```{literalinclude} 4-classad-transfer-files/repl.sh
:language: sh
```

And then submit your job using

```bash
condor_submit repl.ini; tail -F repl.log repl-0.out repl-0.err repl-1.out repl-1.err
```

The `tail` will shows you the status of your job in real time.

:::{note}
We normally won't use the `module` system here, but if needed, notice the shebang `#!/bin/bash -l` is necessary for `module` to be found.
:::

This example also includes some information specific to HTCondor that you can play around.
