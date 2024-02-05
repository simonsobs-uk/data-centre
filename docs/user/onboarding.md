# Onboarding

You will need to

1. have a grid certificate,
2. register to a VO,
3. and obtain a UNIX account.

(obtaining-grid-cert)=
## Grid certificate

Go to [UK Certification Authority Portal](https://portal.ca.grid-support.ac.uk/) and obtain a grid certificate. You will obtain a `certBundle.p12` file which is "an archive file format for storing many cryptography objects as a single file"[^p12]

[^p12]: See [PKCS 12 - Wikipedia](https://en.wikipedia.org/wiki/PKCS_12).

:::{note}
You may need to use a different website if you are outside UK. TODO: add other countries' links here.

Follow the instruction over there to obtain grid certificate. They implements a strong principle of [Web of trust](https://en.wikipedia.org/wiki/Web_of_trust) and requires you to physically verify your identity in-person with an existing member of the Grid.
:::

## Registering the SO:UK Virtual Organization (VO) and obtain a grid certificate

Go to [VOMS Admin > souk.ac.uk](https://voms.gridpp.ac.uk:8443/voms/souk.ac.uk/register/start.action) and submit an application to the VO.

:::{note}
They prefer you to use your institutional email here. It does not have to match your email address used in the Grid Certificate.

Once submitted, you will receive an email. Once you clicked the link in the email to confirm your application, you need to wait for admin to process it.

Occasionally the application went into a blackhole, feel free to ping the admin there or us if you aren't approved in a couple of days.
:::

(obtaining-unix-account)=
## Obtain a UNIX account

Provide the following info and send it to one of us:

0. Your email address, GitHub account name, and preferred name.
1. Your preferred UNIX username. If you don't know, run `echo $USER` in your terminal and copy that.
2. Your first name and last name, same as the one used above.
3. Copy your ssh public key(s) to us. For example, you can run the following commands and copy the first available result:

    ```sh
    cat ~/.ssh/id_ed25519.pub
    cat ~/.ssh/id_rsa.pub
    ```

4. (Optional) if you want to use a password, follow the following procedure to generate a hash. *On your local machine* (`vm77`'s `openssh` is too old), enter this line,

    ```console
    $ openssl passwd -6 -salt $(openssl rand -base64 16)
    # type the password you want to use in the prompt
    # and result would look like this:
    $6$...$...
    ```

    Copy the resulting string to us.

Then email Robert the location of this file (`/opt/$USER` expanded) and telling him that it is your salted, SHA-512 hashed password.

For maintainers to add this new user, go to [this section](#new-users).
