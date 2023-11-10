# Installing Grid File Access Library (GFAL)

Unfortunately, the documentation at [GFAL2 · Data Management Clients Documentation](https://dmc-docs.web.cern.ch/dmc-docs/gfal2/gfal2.html) does not indicate how to install it. You could compile it yourself following [Data Management Clients / gfal2 · GitLab](https://gitlab.cern.ch/dmc/gfal2), or on RHEL:

```sh
sudo yum install 'gfal2*' 'python3-gfal2*'
```

Other package managers might support it. Please provide a pull request / issue helping us to document this.

# Accessing the grid storage system using GFAL

You can now access our grid storage system at

- <davs://bohr3226.tier2.hep.manchester.ac.uk:443//dpm/tier2.hep.manchester.ac.uk/home/souk.ac.uk/>, or
- <root://bohr3226.tier2.hep.manchester.ac.uk:1094//dpm/tier2.hep.manchester.ac.uk/home/souk.ac.uk/>.

:::{warning}
Notice the double slash in `...ac.uk:...//dpm/...`. If a single slash is used, some tools might fail.
:::

For example, to see what's inside,

```bash
gfal-ls -alH --full-time davs://bohr3226.tier2.hep.manchester.ac.uk//dpm/tier2.hep.manchester.ac.uk/home/souk.ac.uk/
# or
gfal-ls -alH --full-time root://bohr3226.tier2.hep.manchester.ac.uk//dpm/tier2.hep.manchester.ac.uk/home/souk.ac.uk/
```

And to make a directory there,

```bash
gfal-mkdir davs://bohr3226.tier2.hep.manchester.ac.uk//dpm/tier2.hep.manchester.ac.uk/home/souk.ac.uk/testing
# or
gfal-mkdir root://bohr3226.tier2.hep.manchester.ac.uk//dpm/tier2.hep.manchester.ac.uk/home/souk.ac.uk/testing
```

To delete it,

```bash
gfal-rm -r davs://bohr3226.tier2.hep.manchester.ac.uk//dpm/tier2.hep.manchester.ac.uk/home/souk.ac.uk/testing
# or
gfal-rm -r root://bohr3226.tier2.hep.manchester.ac.uk//dpm/tier2.hep.manchester.ac.uk/home/souk.ac.uk/testing
```

:::{note}
We omitted the port when gfal is used here, as the default ports are used.
:::

:::{warning}
You can delete files created by others, vice versa. Thing twice before deleting or overwriting. To protect your files, you may use gfal-chmod below.
:::

(gfal)=
## More info

As of writing, the versions of the softwares are

```
gfal-ls v1.7.1
GFAL-client-2.21.5
```

Available commands:

```
gfal2_version
gfal-evict
gfal-mkdir
gfal-sum
gfal-archivepoll
gfal-legacy-bringonline
gfal-rename
gfal-token
gfal-bringonline
gfal-legacy-register
gfal-rm
gfal-xattr
gfal-cat
gfal-legacy-replicas
gfal-save
gfal-chmod
gfal-legacy-unregister
gfal_srm_ifce_version
gfal-copy
gfal-ls
gfal-stat
```

Some of the commands mimics corresponding POSIX commands:

**gfal-mkdir**
: `mkdir`—Creates directories.

**gfal-cat**
: `cat`—Displays the content of a file.

**gfal-chmod**
: `chmod`—Changes file permissions and modes.

**gfal-rm**
: `rm`—Removes files or directories.

**gfal-copy**
: `cp`—Copies files and directories.

**gfal-ls**
: `ls`—Lists files and directories.

**gfal-stat**
: `stat`—Displays detailed information about files and directories.

**gfal-rename**
: `mv`—Renames or moves files and directories.

Check their respective man pages or help string for more information and see available options. For example, run

```bash
man gfal-ls
gfal-ls -h
```
