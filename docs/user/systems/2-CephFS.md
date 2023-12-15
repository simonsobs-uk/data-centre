# The upcoming upgrade to Ceph & CephFS

Transition to CephFS is scheduled in early 2024.

CephFS will provide a similar experience to NERSC's SCRATCH space powered by LUSTRE.
This will replace the clunky grid storage system for data I/O currently powered by DPM with XRootD and xrootdfs.
This will also replace CVMFS for software deployment.

See [transition between pre-production CephFS to production CephFS · Issue #24 · simonsobs-uk/data-centre](https://github.com/simonsobs-uk/data-centre/issues/24).

- Blackett is currently using DPM and will transition into Ceph in 2024.
- Currently, XRootD is serving from DPM, which will transition into serving from Ceph instead.
- Ceph exposes the filesystem via CephFS (currently xrootdfs can be used to mount XRootD as FS via FUSE, but not on worker nodes), available on all nodes including worker nodes.
- pre-production CephFS will be put on our machines (the SO:UK DC purchased machines), but may be subject to purging when transitioning into production
	- This will not be a problem for us (stopping us using pre-production CephFS ASAP), and we plan to copy data for our users. Both can be mounted, and then say we make the pre-production CephFS read-only, and replicates it to the production CephFS. We should provide env. var. to hide the differences in absolute path (see #23)

Link:

- [Ceph Deployment and Monitoring at Lancaster, GridP47, 23 March 2022, Gerard Hand, Steven Simpson, Matt Doidge](https://indico.cern.ch/event/1128343/contributions/4787157/attachments/2411899/4127400/GridPP47LancsCephDeploymentandMonitoring.pdf)

    > There’s only so many times you can declare a million files lost and not rethink all your life choices.
