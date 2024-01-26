# Tips and gotchas when writing HTCondor ClassAds

## Automatic detection of output files to transfer back to submit notes

If `should_transfer_files = YES` is specified, HTCondor has heuristics to automatically transfer **some** files created on the compute node back to your submit node, which can be a surprise to the end users.

`should_transfer_files = NO` is not the best choice however, for [this other reason](#should_transfer_files).

The recommended setup to suppress this behavior is:

```ini
should_transfer_files = YES
transfer_output_files = ""
# optionally, also
when_to_transfer_output = ON_SUCCESS
```

I.e. either specifically set `transfer_output_files` to the list of files and/or directories you need to transfer, or set it to empty string explicitly.

For more details, see [Specifying What Files to Transfer — HTCondor Manual](https://htcondor.readthedocs.io/en/latest/users-manual/file-transfer.html#specifying-if-and-when-to-transfer-files).

(should_transfer_files)=
## Setting `should_transfer_files = No` would prevent jobs from running on some nodes under certain circumstances

From [issue #45](https://github.com/simonsobs-uk/data-centre/issues/45#issuecomment-1911646837):

It looks like HTCondor adds some restrictions to the requirements expression depending on the value of `should_transfer_files`:

-   `IF_NEEDED` (that's also the default):

    ```
    ((TARGET.FileSystemDomain == MY.FileSystemDomain) || (TARGET.HasFileTransfer))
    ```a

-   `YES`:

    ```
    (TARGET.HasFileTransfer)
    ```

-   `NO`:

    ```
    (TARGET.FileSystemDomain == MY.FileSystemDomain)
    ```
    
As we don't have a shared filesystem, all nodes in the cluster have a different value for `MyFileSystemDomain`, it's set to the FQDN of each node. This will change once we have a shared filesystem in place.
