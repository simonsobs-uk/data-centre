# Mounting the grid storage system as a POSIX filesystem

## Installing XRootD

Follow their documentation at [xrootd/xrootd: The XRootD central repository](https://github.com/xrootd/xrootd#installation-instructions).

## Mounting via `xrootdfs`

A wrapper script is provided at `/opt/simonsobservatory/xrootdfs.sh` on `vm77`, and also in this repository.

If you haven't done already, you will need to setup the user-side access on our submit nodes by following the [User credentials](#user-credentials) section.
You will also need to run [Creating a proxy](#creating-a-proxy) periodically.

As usual, you can create a proxy using

```sh
voms-proxy-init --voms souk.ac.uk --valid 168:0
```

This will creates an Attribute Certificate (AC) to `/tmp/x509up_u$UID`.

Once your have this AC set up, you can run `/opt/simonsobservatory/xrootdfs.sh start` to mount it to `~/souk.ac.uk`, and `/opt/simonsobservatory/xrootdfs.sh stop` to unmount it.

:::{warning}
Once your AC expired, you need to go through this section again to re-generate the AC, and run `/opt/simonsobservatory/xrootdfs.sh restart`.
:::

Feel free to modify the wrapper script, as copied below:

```{literalinclude} ../../../../../bin/xrootdfs.sh
:language: sh
```
