# Output (Coming soon)

```{toctree}
:maxdepth: 2
:hidden:
:glob:

5-Output/*
```

We already see how you can transfer any output files from worker nodes in configuring your ClassAd. But this has a limitation that our submit node currently only has ~200GiB and is not suitable to write large amount of files there.

Here we will talk about the *de facto* choice to write large amounts of output files on such grid system—storage elements.
