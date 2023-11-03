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
        groups: simonobservatory
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

2. Tell Robert to update.
