# Accessing the grid storage system from worker nodes

In the last section, we have seen how to connect to the grid storage system from a computer, including the submit nodes that we maintained.

We will now see how it can be accessed from within worker nodes.

If you haven't done already, you will need to setup the user-side access on our submit nodes by following the [User credentials](#user-credentials) section.
You will also need to run [Creating a proxy](#creating-a-proxy) periodically.

As usual, you can create a proxy using

```sh
voms-proxy-init --voms souk.ac.uk --valid 168:0
```

This will creates an Attribute Certificate (AC) to `/tmp/x509up_u$UID`.

## Example job

From now on **we assumes you already created a proxy recently and it has not been expired**.

In the current directory that we are going to submit the job, we will then link the AC to a file here.

```sh
ln -s "/tmp/x509up_u$UID" ac.pem
```

While this is not necessary, this avoids hardcoding the path towards this file in your ClassAd, making sharing ClassAd with collaborators more reproducible.

Now, in `gfal.ini`, we set it up to copy this `ac.pem` to the worker node:

```{literalinclude} 3-accessing-grid-storage-using-HTCondor/gfal.ini
:language: ini
```

And in `gfal.sh`, we use `export X509_USER_PROXY=ac.pem` to inform where our AC is:

```{literalinclude} 3-accessing-grid-storage-using-HTCondor/gfal.sh
:language: sh
```

Note that any gfal commands from [this section](#gfal) can be used so that you can either copy files from the grid storage system to the worker nodes in the beginning of your script, or copy files from the current worker node to the grid storage system by the end of your script.

Lastly, submit and see what happens[^tail]

```bash
condor_submit gfal.ini; tail -F gfal.log gfal.out gfal.err
```

[^tail]: See [](#tail) for an explanation on what the `tail` command does.

After the job finished, you can check your output files copied to the grid storage system, like so

```sh
gfal-ls davs://bohr3226.tier2.hep.manchester.ac.uk//dpm/tier2.hep.manchester.ac.uk/home/souk.ac.uk/$USER/
gfal-cat davs://bohr3226.tier2.hep.manchester.ac.uk//dpm/tier2.hep.manchester.ac.uk/home/souk.ac.uk/$USER/hello-davs.txt
...
```
