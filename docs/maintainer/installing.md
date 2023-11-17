# Installing this project

This project has a few major components:

`docs/`

: documentation of the SO:UK Data Centre with a focus on software deployment.

`src/souk_data_centre/`
: a Python library under the namespace of `souk_data_centre`, intended to be convenient utilities to assist interacting and using the SO:UK Data Centre resource. It is currently empty but is required to be installed in order for the documentation to be built successfully (because API doc is built automatically).

## Installing the environment

### Using `pip`

```sh
python -m pip install .
# or if you want to install in editable mode
python -m pip install -e .
```

### Using `conda`/`mamba` (recommended)

This is the method used to build the documentation here using Continuous Integration such as GitHub Pages and Read the Docs.

1. If you haven't already, install `conda` or `mamba` following your favorite guide.

    A one-liner to install `mamba` to `"$HOME/.mambaforge"` is provided:

    ```sh
    curl -L https://github.com/ickc/bootstrapping-os-environments/raw/master/install/mamba.sh | bash
    ```

2. Install the environment

    ```sh
    mamba env create -f environment.yml
    # or using conda
    conda env create -f environment.yml
    ```

3. Activating the environment

    ```sh
    conda activate soukdc
    ```

4. Install this project

    ```sh
    python -m pip install --no-dependencies .
    # or if you want to install in editable mode
    python -m pip install --no-dependencies -e .
    ```

:::{note}
This is exactly how the environment is prepared in GitHub Pages. See the source of `.github/workflows/sphinx.yml`.
:::
