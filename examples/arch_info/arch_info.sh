#!/usr/bin/env bash

CONDA_PREFIX=/cvmfs/northgrid.gridpp.ac.uk/simonsobservatory/conda/so-conda-py310-latest
. "$CONDA_PREFIX/bin/activate" "$CONDA_PREFIX"

./arch_info.py arch-info "$@"
