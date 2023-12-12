# Installing Grid File Access Library (GFAL)

Unfortunately, the documentation at [GFAL2 · Data Management Clients Documentation](https://dmc-docs.web.cern.ch/dmc-docs/gfal2/gfal2.html) does not indicate how to install it. You could compile it yourself following [Data Management Clients / gfal2 · GitLab](https://gitlab.cern.ch/dmc/gfal2), or on RHEL:

```sh
sudo yum install 'gfal2*' 'python3-gfal2*'
```

Other package managers might support it. Please provide a pull request / issue helping us to document this.

Move on to [](#gfal-access) to see how to use it.
