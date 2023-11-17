(computing-resources)=
# Managing and Maintaining Computing Resources

(new-users)=
## Adding new users

Point the user to [this section](#obtaining-unix-account) and ask them to send those info to you.

1. Edit `/home/dthomas/common.yaml` on `vm77`, replace the following `ALL_CAP` variables accordingly,

    ```yaml
    common::users:
    USER_NAME:
        uid: UID
        comment: FIRST_NAME LAST_NAME
        groups: simonsobservatory
        home: /home/USER_NAME
        keys:
        - 'ssh-ed25519 KEY_VALUE COMMENT'
        password: '$6$...$...'
        groups:
        - sudo
    ```

    :::{note}
    For `UID`, increments according to the list. Just make sure it has not been used.

    For `sudo` groups, obviously only grant those you want them to have sudo privillege.
    :::

2. Tell Robert to update.

## Register as a new content manager (CVMFS)

1. Run `ssh northgridsgm@cvmfs-upload01.gridpp.rl.ac.uk` from any computer. Then you'd see something like

        (northgridsgm@cvmfs-upload01.gridpp.rl.ac.uk) Authenticate at
        -----------------
        https://aai.egi.eu/device?user_code=...
        -----------------
        Hit enter when you have finished authenticating

    Follow the link and register there.

2. On <https://aai.egi.eu/auth/realms/egi/account/#/personal-info>, get your username.

3. Follow [CVMFS - GridPP Wiki](https://www.gridpp.ac.uk/wiki/CVMFS#Request_access) to send an email including the username above as your `voperson_id`:

- Name of the VO or CVMFS repository: northgrid.gridpp.ac.uk
- The “voperson_id” from your account in EGI CheckIn: ...@egi.eu

4. Wait for email from <lcg-support@gridpp.rl.ac.uk> when the admin added you to the service.
