# Writing ClassAd—vanilla universe

To request a job in the parallel universe, create a file `example.ini`,

```{literalinclude} 13-classad-parallel/example.ini
:language: ini
```

And then submit your job using

```bash
condor_submit example.ini; tail -F hello_world.log hello_world-0.out hello_world-0.err hello_world-1.out hello_world-1.err
```

The `tail` will shows you the status of your job in real time.

## Explanation

