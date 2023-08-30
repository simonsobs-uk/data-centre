{#running-pipelines}
# Running pipelines

```{toctree}
:maxdepth: 2
:hidden:
:glob:

pipeline/*
```

The typical life-cycle of a workflow / pipeline are

1. Write a job configuration file and submit it to the workload manager,
    - which typically include a job script, say written in bash, as well.
2. Bootstrap a software environment on the worker node.
3. (Optionally) launch MPI applications using the provided wrapper in parallel universe.
4. I/O:
    - Reading data, as the input of your application,
    - Writing and storing data, as the product of your application.

In the following sections, we will go through these one by one. Per stage, there exists multiple solutions or situations that we will go through. In the end, we will provide example workflows where each touches all these aspects.
