# Introduction to CVMFS

C.f. [](#cvmfs-simple).

Properties of CVMFS:

- POSIX read-only file system
- user space (FUSE module)
- shares a universal namespace under `/cvmfs/...`
- world readable
- content managers: only special users who registered as content managers can write to this space (See [](#content-manager-registration) and [](#CVMFS-pub).)
- synchronization lag: it takes some time for it to be synchronized from the publishing node. Empirically, it takes around 3 hours for contents to be sync'd on Blackett.
- world-readable: Anyone can see the contents so no secrets should be placed here.
