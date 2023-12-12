# SO:UK Data Centre Systems

## Worker nodes at Blackett

As the SO:UK Data Centre is part of Blackett, we have access to [its Tier-2 services](https://www.blackett.manchester.ac.uk/services/). This means by default when we submit jobs from HTCondor, we can have access to the facility as well, where its main users are from ATLAS and LHCb.

We will have more detailed documentation on the Blackett architecture later. Meanwhile, we will start with documenting its wall-clock time, copied from [Feedback on user documentation · Issue #14 · simonsobs-uk/data-centre](https://github.com/simonsobs-uk/data-centre/issues/14).

- There's a maximum wall-clock time configured. It's currently **72 hours**, jobs get killed if they exceed this.
- The same is true for CPU time for each requested CPU (ie job gets killed if `total used CPU hours > requested CPUs * 72 hours`)
- Need to check how the machine count fits into this, we'll most likely have to update the configuration to take this into account (ie `machine count * requested CPUs * 72 hours`).

## SO:UK Data Centre worker nodes (Coming Soon)

## Submit node

Our submit node is `vm77`, a single, small VM instance for submitting jobs. This is where you ssh into.

## JupyterHub (Coming Soon)

See [Establishing a Dedicated Login Node for Interactive Computing and JupyterHub Integration · Issue #31 · simonsobs-uk/data-centre](https://github.com/simonsobs-uk/data-centre/issues/31).
