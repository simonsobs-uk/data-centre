{#0-transfer-output-files}
# Transferring files via ClassAd using HTCondor

We already saw how we can use ClassAd with HTCondor to transfer files from submit node to worker nodes.

For the other direction (from worker nodes back to submit node), you can specify this in the ClassAd to transfer output files, for example,

```ini
transfer_output_files = schedules,out_f090_i1_Jupiter
```

These comma-separated paths can be files or directories, and in case of directories, the entirety of the contents within will be transferred back to the submit node.

:::{note}
This is not a recommended method to transfer large amount of data, as the submit node only has ~200GiB of local storage.
:::
