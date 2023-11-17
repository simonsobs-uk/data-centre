# Writing & building documentation

The main framework of choice to write and build documentation in this project is the [Sphinx documentation generator](https://www.sphinx-doc.org/en/master/), with the contents authored in markdown with the [parser MyST](https://myst-parser.readthedocs.io/en/latest/). As RST is natively supported in Sphinx, you can also authored in RST.

## Syntax

Markdown syntax are generally supported. One important note is how to include new files in the TOC tree. For example, in `maintainer.md`, the following `toctree` directive is used to include this file.

    ```{toctree}
    :maxdepth: 2
    :hidden:

    maintainer/installing
    maintainer/documenting
    maintainer/releasing
    ```

If a new file is not included in a `toctree`, you will see a warning when building the documentation. A glob pattern can be used to include files implicitly, such as

    ```{toctree}
    :maxdepth: 2
    :hidden:
    :glob:

    pipeline/*
    ```

## Structure

The following is the tree structure as of writing. It borrows a subpage concept from Notion. For example, `maintainer.md` has an accompanying `maintainer/` directory, which includes some more source files such as `documenting.md`. This indicates that `documenting.md` "belongs" to (or is a subpage of) `maintainer.md`.

```console
docs
├── changelog.md
├── conf.py
├── developer
│   ├── htcondor-glossary.md
│   ├── tips
│   │   ├── monitor.md
│   │   └── tail.md
│   └── tips.md
├── developer.md
├── index.md
├── maintainer
│   ├── computing-resources.md
│   ├── documenting.md
│   ├── installing.md
│   └── releasing.md
├── maintainer.md
├── user
│   ├── onboarding.md
│   ├── pipeline
│   │   ├── 1-classad
│   │   │   ├── 1-classad-interactive
│   │   │   │   ├── example.ini
│   │   │   │   └── makefile
│   │   │   ├── 1-classad-interactive.md
│   │   │   ├── 2-classad-vanilla
│   │   │   │   ├── example.ini
│   │   │   │   └── makefile
│   │   │   ├── 2-classad-vanilla.md
│   │   │   ├── 3-classad-parallel
│   │   │   │   ├── example.ini
│   │   │   │   └── makefile
│   │   │   ├── 3-classad-parallel.md
│   │   │   ├── 4-classad-transfer-files
│   │   │   │   ├── makefile
│   │   │   │   ├── repl.ini
│   │   │   │   └── repl.sh
│   │   │   ├── 4-classad-transfer-files-2
│   │   │   │   ├── cat.ini
│   │   │   │   ├── cat.txt
│   │   │   │   └── makefile
│   │   │   └── 4-classad-transfer-files.md
│   │   ├── 1-classad.md
│   │   ├── 2-software-deployment
│   │   │   ├── 1-tarball
│   │   │   │   ├── makefile
│   │   │   │   ├── tarball.ini
│   │   │   │   └── tarball.sh
│   │   │   ├── 1-tarball.md
│   │   │   └── 2-CVMFS.md
│   │   ├── 2-software-deployment.md
│   │   ├── 3-MPI-applications
│   │   │   ├── 1-OpenMPI
│   │   │   │   ├── env.sh
│   │   │   │   ├── makefile
│   │   │   │   ├── mpi.ini
│   │   │   │   └── mpi.sh
│   │   │   └── 1-OpenMPI.md
│   │   ├── 3-MPI-applications.md
│   │   ├── 4-IO
│   │   │   ├── 0-transfer-via-ClassAd.md
│   │   │   ├── 1-grid-storage-system.md
│   │   │   └── 2-librarian.md
│   │   └── 4-IO.md
│   ├── pipeline.md
│   └── quick-start.md
└── user.md

19 directories, 53 files
```

## More details

See `pyproject.toml` or `environment.yml` to see the dependencies in Python. See `docs/conf.py` to see the extensions enabled in Sphinx.
