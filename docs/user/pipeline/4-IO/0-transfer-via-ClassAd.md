{#0-transfer-output-files}
# Transfer output files

You can specify this in the ClassAd to transfer output files, for example,

```ini
transfer_output_files = schedules,out_f090_i1_Jupiter
```

These comma-separated paths can be files or directories, and in case of directories, the entirety of the contents within will be transferred back to the submit node.

:::{note}
This is not a recommended method to transfer large amount of data, as the submit node only has ~200GiB of local storage.
:::
