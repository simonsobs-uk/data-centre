(computing-resources)=
# Managing and Maintaining Computing Resources

## New accounts

(new-users)=
### Adding new users on the submit node `vm77`

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

(content-manager-registration)=
### Register as a new content manager (CVMFS)

1. Run `ssh northgridsgm@cvmfs-upload01.gridpp.rl.ac.uk` from any computer. Then you'd see something like

        (northgridsgm@cvmfs-upload01.gridpp.rl.ac.uk) Authenticate at
        -----------------
        https://aai.egi.eu/device?user_code=...
        -----------------
        Hit enter when you have finished authenticating

    Follow the link and register there.

2. On <https://aai.egi.eu/auth/realms/egi/account/#/personal-info>, copy the content of "Username" field.

3. Follow [CVMFS - GridPP Wiki](https://www.gridpp.ac.uk/wiki/CVMFS#Request_access) to send an email including the username above as your `voperson_id`:

- Name of the VO or CVMFS repository: `northgrid.gridpp.ac.uk`
- The “voperson_id” from your account in EGI CheckIn: ...@egi.eu

4. Wait for email from <lcg-support@gridpp.rl.ac.uk> when the admin added you to the service.

## Software deployments

### Publishing to CVMFS

See [above](#content-manager-registration) if you haven't applied for the role of content manager yet.

Then

```sh
ssh northgridsgm@cvmfs-upload01.gridpp.rl.ac.uk
```

Then starts to write something in `~/cvmfs_repo/simonsobservatory`. What you write will immediately be available at `/cvmfs/northgrid.gridpp.ac.uk/simonsobservatory` on this publishing node. But it will only be synchronized to other sites with a time scale of around 1 hour.

On `vm77`, check if you see your stuffs is in `/cvmfs/northgrid.gridpp.ac.uk/simonsobservatory` already, if so, you can start to submit jobs that reads from there.

## Monitoring

### `condor_status`

```sh
# list all nodes in the pool along with their basic status information
sudo condor_status
# for more detailed information about each node
sudo condor_status -long
# see available nodes after constraints
sudo condor_status -constraint 'Arch == "x86_64"'
# Lists available nodes
condor_status -avail
# Lists only the machine names
sudo condor_status -format "%s\n" Machine | sort -u
```
