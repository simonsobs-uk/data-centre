(tarball-deployment)=
# The tarball method

We will start by explaining the concept of `PREFIX` directory, and then provide an example utilizing this concept and the machinery around the conda ecosystem. We will also provide a starter tarball that you can feel free to use and modified from.

## `PREFIX` directory and software deployment

`PREFIX` directory refers to a directory within which a piece of software is installed into. Usually, there are a few directories inside this prefix among others, such as `bin`, `lib`, `share`. For example, `bash` is typically installed under the prefix `/usr`.

The complication which arises in software deployment from one computer (such as submit node or your local machine) to another computer is that the followings must match:

1. OS, say Linux,
2. CPU architecture, such as x86-64 (also known as x64, x86_64, AMD64, and Intel 64),
3. prefix directory,
4. any other dependencies outside this prefix directory.

We will not talk about cross-compilation here, so we assume (1) & (2) matches already. E.g. you have a local machine running x86-64 Linux and deploying software to our data centre.

The reason prefix directory has to match is that not all software is designed to be portable. Unless you are sure the software you installed or the application you are developing is designed to be portable, you should assume it is not.

(4) can also creates complications, as if no extra care is given, your softwares inside the prefix directory will most likely depends on other things, such as dynamically linked libraries, outside the prefix directory. In this situation, if you archive your prefix directory to a tarball and ship it to a worker node, it can complains about missing dynamically linked libraries for example.

To solve (3) & (4), we utilizes the heavy machinery from conda which enables one to create a conda environment to any prefix directory of your choice, and bundle all the necessary dependencies within that prefix directory such that this prefix directory is now *self-contained*.

The last piece of the puzzle is to choose a prefix directory that both your local machine and all the worker nodes has write access to. Here we abuse the `/tmp` directory as this always exists and writable.

:::{note}
`/tmp` are local to an HTCondor process, so even if your job might be sharing the same physical node with another job, they have their own `/tmp` directory and therefore it would not be interfered.
:::

The provided tarball below is doing exactly this. And if you want to deploy your own applications, be sure to follow these advices to avoid any potential problems.

## Example

create a file `tarball.ini`,

```{literalinclude} 1-tarball/tarball.ini
:language: ini
```

This ClassAd uses `transfer_input_files` to transfer a tarball from the submit node to the worker node.

:::{warning}
The path `/opt/simonobservatory/pmpm-20230718-Linux-x86_64-OpenMPI.tar.gz` is provided by us and may be changed over time. Try `ls /opt/simonobservatory` to see available tarballs. File an issue if what you're seeing in the documentation is outdated.
:::

The ClassAd involve a script `tarball.sh`,

```{literalinclude} 1-tarball/tarball.sh
:language: sh
```

Here you see that the tarball is unarchived to `/tmp`, and then the conda environment is activated explicitly using `. "$PREFIX/bin/activate" "$PREFIX"` (`PREFIX=/tmp/pmpm-20230718` in this specific example).

And then you can submit your job using

```bash
condor_submit tarball.ini; tail -F tarball.log tarballs.out tarball.err
```

The `tail` will shows you the status of your job in real time.

:::{note}
We would note that in this specific example, it takes around 50s to unarchive the environment. So for long running jobs this becomes negligible. But if you starts multiple short running jobs, this is not an optimal method to deploy software.
:::

## "Forking" the provided tarball

You can modifies our provided tarball to your liking by following the above example and unarchive it under `/tmp` and activate it `. "$PREFIX/bin/activate" "$PREFIX"`. Here you can start to install more packages by using either `mamba install ...`, `conda install ...` or `pip install ...`.

Once your environment is ready,

```sh
# PREFIX=pmpm-20230718 in this example
cd /tmp; tar -cf "$PREFIX-Linux-x86_64-NAME.tar" "$PREFIX"
gzip "$PREFIX-Linux-x86_64-NAME.tar"
```

Now you can transfer this tarball to the submit node first (say via `rsync` or `wget`/`curl`), and then specify that in your ClassAd with `transfer_input_files`.

:::{warning}
Do not do this on the submit node. Firstly because submit node is for submission only and is very resource constrained, and also because in the submit node everyone is sharing the same `/tmp` directory. A recommended to do this is to first request an interactive node and works from there. Alternatively, do it in a dedicated Linux machine.
:::
