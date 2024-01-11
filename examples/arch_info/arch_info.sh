#!/usr/bin/env bash

CONDA_PREFIX=/cvmfs/northgrid.gridpp.ac.uk/simonsobservatory/opt/all310-conda-forge
. "$CONDA_PREFIX/bin/activate" "$CONDA_PREFIX"

./arch_info.py "$@"
