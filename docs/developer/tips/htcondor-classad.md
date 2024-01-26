# Tips and gotchas when writing HTCondor ClassAds

## Automatic detection of output files to transfer back to submit notes

If `should_transfer_files = YES` is specified, HTCondor has heuristics to automatically transfer **some** files created on the compute node back to your submit node, which can be a surprise to the end users.

`should_transfer_files = NO` is not the best choice however, for [this other reason](#TODO).

The recommended setup to suppress this behavior is:

```ini
should_transfer_files = YES
transfer_output_files = ""
# optionally, also
when_to_transfer_output = ON_SUCCESS
```

I.e. either specifically set `transfer_output_files` to the list of files and/or directories you need to transfer, or set it to empty string explicitly.

For more details, see [Specifying What Files to Transfer — HTCondor Manual](https://htcondor.readthedocs.io/en/latest/users-manual/file-transfer.html#specifying-if-and-when-to-transfer-files).
