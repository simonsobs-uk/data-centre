(System-specifications)=
# System specifications

Currently, our testbed includes the following nodes.
Note that some nodes can be submitted via vanilla universe only,
parallel universe only,
or both.

|                                           | CPU model                                 | CPU vendor   | CPU generation | CPU microarchitecture | No. of sockets | Total no. of logical cores | Total no. of physical cores | Total memory (GiB) | Total swap (GiB) | vanilla universe | parallel universe |
| ----------------------------------------- | ----------------------------------------- | ------------ | -------------- | --------------------- | -------------- | -------------------------- | --------------------------- | ------------------ | ---------------- | ---------------- | ----------------- |
| hostname                                  |                                           |              |                |                       |                |                            |                             |                    |                  |                  |                   |
| `wn3805340.tier2.hep.manchester.ac.uk`    | Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz | GenuineIntel | broadwell      | x86_64_v3             | 2              | 16                         | 16                          | 63                 | 64               | True             | False             |
| `wn3805341.tier2.hep.manchester.ac.uk`    | Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz | GenuineIntel | broadwell      | x86_64_v3             | 2              | 16                         | 16                          | 63                 | 64               | True             | False             |
| `wn3806200.tier2.hep.manchester.ac.uk`    | Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz | GenuineIntel | broadwell      | x86_64_v3             | 2              | 32                         | 16                          | 63                 | 64               | False            | True              |
| `wn3806201.tier2.hep.manchester.ac.uk`    | Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz | GenuineIntel | broadwell      | x86_64_v3             | 2              | 32                         | 16                          | 63                 | 64               | False            | True              |
| `wn3806240.tier2.hep.manchester.ac.uk`    | Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz  | GenuineIntel | skylake_avx512 | x86_64_v4             | 2              | 64                         | 32                          | 187                | 64               | True             | True              |
| `wn3806241.tier2.hep.manchester.ac.uk`    | Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz  | GenuineIntel | skylake_avx512 | x86_64_v4             | 2              | 64                         | 32                          | 187                | 64               | True             | True              |
| `wn3806250.tier2.hep.manchester.ac.uk`    | Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz  | GenuineIntel | skylake_avx512 | x86_64_v4             | 2              | 64                         | 32                          | 187                | 64               | True             | True              |
| `wn3806251.tier2.hep.manchester.ac.uk`    | Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz  | GenuineIntel | skylake_avx512 | x86_64_v4             | 2              | 64                         | 32                          | 187                | 64               | True             | True              |
| `wn3806290.tier2.hep.manchester.ac.uk`    | Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz  | GenuineIntel | skylake_avx512 | x86_64_v4             | 2              | 64                         | 32                          | 187                | 64               | False            | True              |
| `wn3806291.tier2.hep.manchester.ac.uk`    | Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz  | GenuineIntel | skylake_avx512 | x86_64_v4             | 2              | 64                         | 32                          | 187                | 64               | False            | True              |
| `wn3806300.tier2.hep.manchester.ac.uk`    | Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz  | GenuineIntel | skylake_avx512 | x86_64_v4             | 2              | 64                         | 32                          | 187                | 64               | False            | True              |
| `wn3806301.tier2.hep.manchester.ac.uk`    | Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz  | GenuineIntel | skylake_avx512 | x86_64_v4             | 2              | 64                         | 32                          | 187                | 64               | False            | True              |
| `wn5914090.in.tier2.hep.manchester.ac.uk` | Intel(R) Xeon(R) Gold 5222 CPU @ 3.80GHz  | GenuineIntel | cascadelake    | x86_64_v4             | 2              | 16                         | 8                           | 1511               | 128              | True             | True              |
| `wn5914340.in.tier2.hep.manchester.ac.uk` | Intel(R) Xeon(R) Gold 5215L CPU @ 2.50GHz | GenuineIntel | cascadelake    | x86_64_v4             | 2              | 40                         | 20                          | 3023               | 128              | False            | True              |
| `wn5916090.in.tier2.hep.manchester.ac.uk` | Intel(R) Xeon(R) Gold 5222 CPU @ 3.80GHz  | GenuineIntel | cascadelake    | x86_64_v4             | 2              | 16                         | 8                           | 1511               | 128              | True             | True              |
| `wn5916340.in.tier2.hep.manchester.ac.uk` | Intel(R) Xeon(R) Gold 5222 CPU @ 3.80GHz  | GenuineIntel | cascadelake    | x86_64_v4             | 2              | 16                         | 8                           | 1511               | 128              | True             | True              |
| `wn5917090.in.tier2.hep.manchester.ac.uk` | Intel(R) Xeon(R) Gold 5222 CPU @ 3.80GHz  | GenuineIntel | cascadelake    | x86_64_v4             | 2              | 16                         | 8                           | 1511               | 128              | False            | True              |

## Constraining jobs to run on a subset of available nodes

This information can be used to [write ClassAd constraints](https://htcondor.readthedocs.io/en/latest/man-pages/condor_submit.html#requirements).
For example,

```ini
requirements = (machine == "wn1905340.in.tier2.hep.manchester.ac.uk`") || (machine == "wn5914090.in.tier2.hep.manchester.ac.uk`") || (machine == "wn5916090.in.tier2.hep.manchester.ac.uk`") || (machine == "wn5916340.in.tier2.hep.manchester.ac.uk`") || (machine == "wn5914340.in.tier2.hep.manchester.ac.uk`") || (machine == "wn5917090.in.tier2.hep.manchester.ac.uk`")
```
