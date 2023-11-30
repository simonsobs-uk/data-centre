# Logging into our submit node `vm77`

From the username you got from [the previous section](#obtaining-unix-account), here by named `$USER`,
you now should be able to

```sh
ssh $USER@vm77.tier2.hep.manchester.ac.uk
```

and land into our submit node `vm77`.

## Setting up ssh config

The recommended way to connect to our submit node would be to edit your ssh config file at `~/.ssh/config` and add these lines,
(change `$USER` to your actual username here, and you can skip this line if your client machine is of the same username.)

```
Host blackett
    HostName vm77.tier2.hep.manchester.ac.uk
    User $USER
    IdentityFile ~/.ssh/id_ed25519.pub

# this is for ssh into worker nodes on Blackett which loads its own temporary keys
Host condor-job.*
    IdentitiesOnly yes
    AddKeysToAgent no
```

Replace `~/.ssh/id_ed25519.pub` with `~/.ssh/id_rsa.pub` if necessary, matching the one you sent to us from [the previous section](#obtaining-unix-account).

You can then `ssh blackett` instead.
