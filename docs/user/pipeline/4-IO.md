# Reading and writing data

```{toctree}
:maxdepth: 2
:hidden:
:glob:

4-IO/*
```

For reading data, we already see how you can transfer your job scripts and any files from ClassAd. Here we will provide one more option for you to load SO specific Librarian Books.

For writing data, we will see how you can transfer any output files from worker nodes in configuring your ClassAd. But this has a limitation that our submit node currently only has ~200GiB and is not suitable to write large amount of files there.

Then we will talk about the *de facto* choice to write large amounts of output files on such grid system—the grid storage system.
