# Software deployment

```{toctree}
:maxdepth: 2
:hidden:
:glob:

2-software-deployment/*
```

In this section we will focus on different methods to deploy software to the worker nodes.

Examples used in this section can also be found under `2-software-deployment/` in this repository relative to this file.

The *de facto* way to deploy software on CERN compatible grid system including Blackett where our data centre resides in is via CVMFS. Container technologies are also available, but HTCondor imposes a huge limitation as universes are mutually exclusive, and therefore you cannot put a job in docker/container universe while in parallel universe. As multi-nodes parallelism is important for CMB data analysis, we will not cover container here, although you are welcome to try as a developer. Note that CVMFS is mounted as read-only on the worker nodes, and can only deployed by people with elevated privilege. So CVMFS is for production only and is of limited use for development. Lastly, we will also mention a recommended way to deploy any softwares by packaging things in a tarball and transfer it to the worker nodes.

|  Deployment Method  |  Description                                                                                           |  Suitable For         |  Limitations                                               | Support level                                                                                                                                                                |
|:--------------------|:-------------------------------------------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **Tarball**        |  Packaging software and its dependencies in a compressed format, then transferring to worker nodes.    |  Custom software      |  Manual management; Transfer overhead.                     | Documentation provided to enable you as a developer to control your stack.                                                                                                   |
|  **CVMFS**          |  Standardized software distribution system used in CERN's grid.                                        |  Production software  |  Read-only; Needs elevated privilege for deployment.       | Software deployment is centrally maintained, deployed periodically. You can requests softwares to be included, and approvals will be granted based on technical limitations. |
|  **Containers**     |  Use of technologies like Docker to encapsulate software in isolated environments.                     |  Development, Testing |  Cannot be used with the `parallel` universe in HTCondor.  | Not supported but you can feel free to try when multi-node parallelism is not needed.                                                                                        |  
