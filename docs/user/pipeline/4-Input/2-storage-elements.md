# Storage elements
Manually Transfer files to Storage.

Here is the instruction to copy files to / from the storage on the login node (vm77)

To Transfer the file you need to:
- Convert your certificate .p12 into two pem files (usercert.pem, userkey.pem)
- copy both to the login node and put them into $HOME/.globus/
- run 'voms-proxy-init-voms vo.northgrid.ac.uk' to get voms proxy (it will only active for 24 hours)
- use gfal tools to access the storage, the base url for northgrid is:
- protocol://bohr3226.tier2.hep.manchester.ac.uk/dpm/tier2.hep.manchester.ac.uk/home/vo.northgrid.ac.uk
-crete your own directory trees under the base url
-gfal tool names follow standard unix tools, e.g gfal-ls, gfal-mkdir, gfal-copy, etc
- *use either root or https as a protocol.
