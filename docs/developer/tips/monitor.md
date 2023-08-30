{#monitor-your-jobs}
# Monitor your jobs

In HTCondor, you can use

```sh
condor_q
```

to see the status of your job.

You can also watch them, like so

```sh
watch -n 15 condor_q
```

where 15 is the number of seconds you want the command to be repeated, i.e. you are monitoring the status once every 15s.

There is also a command from HTCondor which do the watching automatically:

```sh
condor_watch_q
```

Both approach has their pros and cons and you are welcome to try which one suits your purpose better.
