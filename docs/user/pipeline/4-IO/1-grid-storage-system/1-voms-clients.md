(user-credentials)=
# User credentials

This part needed to be done once per machine.

You need to have your grid certificate `certBundle.p12` ready that you obtained from [this section](#obtaining-grid-cert). Then run

```sh
mkdir -p "$HOME/.globus/"
mv certBundle.p12 "$HOME/.globus/usercred.p12"
chmod 600 "$HOME/.globus/usercred.p12"
```

(creating-a-proxy)=
# Creating a proxy

This part needed to be done periodically.

```sh
voms-proxy-init --voms souk.ac.uk --valid 168:0
```

> The command `voms-proxy-init` is used to contact the VOMS server and retrieve an Attribute Certificate (AC) containing user attributes that will be included in the proxy certificates.

The Attribute Certificate (AC) is configured with a maximum validity of 168 hours (7 days).

Example output after running this command will be:

```
$ voms-proxy-init --voms souk.ac.uk --valid 168:0
Enter GRID pass phrase for this identity:
Contacting voms03.gridpp.ac.uk:15519 [/C=UK/O=eScience/OU=Imperial/L=Physics/CN=voms03.gridpp.ac.uk] "souk.ac.uk"...
Remote VOMS server contacted succesfully.


Created proxy in /tmp/x509up_u$UID.

Your proxy is valid until Tue Nov 14 08:45:38 GMT 2023
```

The path `/tmp/x509up_u$UID` will be useful later. You can also run `voms-proxy-info --all` and see it again in the `path` attributes.
