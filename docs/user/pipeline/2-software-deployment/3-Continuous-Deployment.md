(continuous-deployment)=
# Continuous Deployment (CD)

:::{note}
Continuous deployment (CD) is actively being developed. It may changes in the future.
:::

Currently, CD is done via GitHub Actions in this repository: [so-software-environment](https://github.com/ickc/so-software-environment).

You can find the latest releases in <https://github.com/ickc/so-software-environment/releases/latest>.

## Explanations of different environments

`PREFIX`
: `cvmfs_northgrid.gridpp.ac.uk_simonsobservatory`: for deploying to CVMFS by Content Managers, see [](#cvmfs-simple) and [](#OpenMPI-CVMFS) for examples.
: `tmp`: for deploying to `/tmp` directory, see [](#tarball-deployment) for examples.

Environment type
: `so-conda`: a (pure) conda environment as defined in [so-software-environment/examples/so.yml](https://github.com/ickc/so-software-environment/blob/main/examples/so.yml)
: `so-pmpm`: a conda environment with some packages compiled and optimized for specific architectures, utilizing [pmpm—Python manual package manager](https://python-pmpm.readthedocs.io/en/latest/). Currently, only `libmadam` and `toast3` are compiled here.

Python version
: The `py310` string means Python 3.10. In principle we can deploy to 3.8, 3.9, 3.10 where some SO packages are currently still incompatible with 3.11, 3.12. We will only support Python 3.10 for now, and look into supporting newer versions of Python as packages become ready.

MKL
: `mkl`: uses Intel MKL.
: `nomkl`: uses openblas instead. AMD CPUs should uses these environments. MKL runs slower on AMD CPUs unless some form of hack is used to disguise AMD CPUs into Intel's.

`x86-64-v?`
: [Microarchitecture levels](https://en.wikipedia.org/wiki/X86-64#Microarchitecture_levels). We currently only support `x86-64-v3`, `x86-64-v4`.
You should only use `x86-64-v4` for those that supports AVX-512, such as all recent Intel Xeon CPUs or AMD Zen 4. While AMD's approach of double pumped AVX-512 implementation does not offers a factor of 2 speed up, but the availability of newer instructions from AVX-512 would still offers small amount of speed up. In short, `x86-64-v4` is recommended for AMD Zen 4.

MPI implementation
: MPICH:

    > MPICH is one of the most popular implementations of MPI. It is used as the foundation for the vast majority of MPI implementations, including IBM MPI (for Blue Gene), Intel MPI, Cray MPI, Microsoft MPI, Myricom MPI, OSU MVAPICH/MVAPICH2, and many others. From [MPICH - Wikipedia](https://en.wikipedia.org/wiki/MPICH#History).
: [Open MPI](https://en.wikipedia.org/wiki/Open_MPI) is an alternative implementation of MPI. This is currently the only supported MPI implementation by us. See [](#cvmfs-simple) and [](#OpenMPI-CVMFS) for examples.

## Examples

To choose an environment for the tarball method where you want to develop the packages and update it, the simplest choice is <https://github.com/ickc/so-software-environment/releases/download/20231214/tmp_so-conda-py310-20231214.tar.gz>. Change the date `20231214` to whichever one you want (today's date for example).

To pick one from the CVMFS, you can see which ones are available first:

```sh
ls /cvmfs/northgrid.gridpp.ac.uk/simonsobservatory/pmpm
```

The example given in [](#OpenMPI-CVMFS) uses `/cvmfs/northgrid.gridpp.ac.uk/simonsobservatory/pmpm/so-pmpm-py310-mkl-x86-64-v3-openmpi-20231212`. Feel free to change the date here.

## Automatic dispatch (Coming soon)

A wrapper will be created to auto-dispatch between `mkl` and `nomkl` versions, and between `x86-64-v3` and `x86-64-v4` versions based on the CPU of the worker nodes.
