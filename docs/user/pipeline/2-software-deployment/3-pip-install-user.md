# Modifying our maintained software environments for software development

When you are using the provided software environments provided by us,
you may still want to add more packages that you use,
perhaps one that you are developing,
that are not currently maintained by us.
This includes the case that it might be a new change you are making
that is not merged in a released version (such as a GitHub Pull Requests you're working on).

In these cases, if this package is something you can install via pip,
this section provide a method to install it inside your job.

We will see how it works in the following example.

## Example

create a file `pip-install-user.ini`,

```{literalinclude} 3-pip-install-user/pip-install-user.ini
:language: ini
```

The ClassAd involve a script `pip-install-user.sh`,

```{literalinclude} 3-pip-install-user/pip-install-user.sh
:language: sh
```

This example uses a package `souk` that was not in the original environment
to demonstrate how this method works.

This uses `pip install --user ...` to install a package locally
without having write access to our provided environment.

Note that this method includes not only a package listed in PyPI,
but also a GitHub branch, such as

```sh
pip install --user https://github.com/simonsobs-uk/data-centre/archive/master.zip
```

As usual, you can submit the job via

```sh
condor_submit pip-install-user.ini
```

See [](#monitor-your-jobs) to see how to monitor the status of your job. For advance use, use this command instead,

```sh
condor_submit pip-install-user.ini; tail -F pip-install-user.log pip-install-user.out pip-install-user.err
```

and see [](#tail) for an explanation on what it does.
