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

# this is for ssh into worker nodes on Blackett which loads its own temporary keys
Host condor-job.*
    IdentitiesOnly yes
    AddKeysToAgent no
```

You can then `ssh blackett` instead.

:::{tip}
If you cannot log in at this point,
first, check which key is the one you sent to us from [the previous section](#obtaining-unix-account).
For example, if the key you sent starts with `ssh-ed25519`,
then probably you are using `~/.ssh/id_ed25519.pub`.
If it starts with `ssh-rsa`,
then probably you are using `~/.ssh/id_rsa.pub`.

You can also list all your available keys by running this command:

```sh
 find ~/.ssh -name '*.pub'
```

Knowing that, you can add a line specifying `IdentityFile` to your ssh config:

```
Host blackett
    HostName vm77.tier2.hep.manchester.ac.uk
    User $USER
    IdentityFile ~/.ssh/id_ed25519
...
```

Replace `id_ed25519` with `id_rsa` if you sent us a `ssh-rsa` key instead.

If it still does not work for you, run the below command and send us the text file `ssh-debug.txt`:

```sh
find ~/.ssh -name '*.pub' > ssh-debug.txt
echo '===' >> ssh-debug.txt
cat ~/.ssh/config >> ssh-debug.txt
echo '===' >> ssh-debug.txt
ssh blackett -vvv >> ssh-debug.txt 2>&1
```
:::
