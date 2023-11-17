# Advanced usage: use XRootD to interact with the grid storage system directly

Rather than using GFAL, you could access via the XRootD protocol directly. For example,

```sh
XROOTDFS_RDRURL='root://bohr3226.tier2.hep.manchester.ac.uk:1094//dpm/tier2.hep.manchester.ac.uk/home/souk.ac.uk/'
echo 'Hello world' > /tmp/test
xrdcp /tmp/test "$XROOTDFS_RDRURL/$USER-test"
rm -f /tmp/test
```

And it can also be used interactively, which provides a POSIX filesystem-like experience:

```console
# this command enters an interactive mode
$ xrdfs bohr3226.tier2.hep.manchester.ac.uk 
# how you can ls
[bohr3226.tier2.hep.manchester.ac.uk:1094] / > ls
/SRR
/atlas
/bes
/biomed
/cms
/dteam
/dune
/euclid.net
/eucliduk.net
/fermilab
/gridpp
/hone
/icecube
/ilc
/lhcb
/lsst
/lz
/ops
/pheno
/skatelescope.eu
/souk.ac.uk
/t2k.org
/vo.northgrid.ac.uk
# or cd
[bohr3226.tier2.hep.manchester.ac.uk:1094] / > cd souk.ac.uk
[bohr3226.tier2.hep.manchester.ac.uk:1094] /souk.ac.uk > ls
/souk.ac.uk/erosenberg
```

## Definitions

`xrdcp`
: This command is akin to the POSIX `cp` command. It's used for copying files and directories within XRootD or between XRootD and local file systems.

`xrdfs`
: This command can be compared to various POSIX file system commands. It allows users to interact with a remote file system using operations similar to those found in POSIX, like listing directories, creating/removing files, etc.
