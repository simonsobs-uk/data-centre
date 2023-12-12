# 2023-11-13 SO:UK BB "see what's what & get involved" day—Introduction to the SO:UK Data Centre

:::{note}
Initially presented on 2023-11-13 shortly after the v0.2.0 release of the SO:UK Data Centre documentation. See [](#changelog) to see what's changed since then.
:::

<iframe width="560" height="315" src="https://www.youtube.com/embed/sGxCepKCJxA?si=7XZunOu-gebwIa9k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Big picture (Why)

### HPC vs. HTC

According to the European Grid Infrastructure (EGI):

High Throughput Computing (HTC)
: A computing paradigm that focuses on the efficient execution of a large number of **loosely-coupled tasks**. Given the **minimal parallel communication requirements**, the tasks can be executed on clusters or physically distributed resources using grid technologies. HTC systems are typically optimised to maximise the throughput over a long period of time and a typical metric is jobs per month or year.

High Performance Computing (HPC)
: A computing paradigm that focuses on the efficient execution of **compute intensive, tightly-coupled tasks**. Given the high parallel communication requirements, the tasks are typically executed on **low latency interconnects** which makes it possible to **share data very rapidly** between a large numbers of processors working on the same problem. HPC systems are delivered through low latency clusters and supercomputers and are typically optimised to maximise the number of operations per seconds. The typical metrics are FLOPS, tasks/s, I/O rates.

- [High Throughput Computing - EGI Glossary - EGI Confluence](https://confluence.egi.eu/pages/viewpage.action?pageId=86278641)
- [High Performance Computing - EGI Glossary - EGI Confluence](https://confluence.egi.eu/pages/viewpage.action?pageId=86278639)

|                          | HTC                                                             | HPC                                                                                 |
| ------------------------ | --------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Optimized for            | loosely-coupled tasks                                           | tightly-coupled tasks                                                               |
| interconnects            | high latency, low bandwidth (e.g. 10Gbps)                       | low latency, high bandwidth (e.g. InfiniBand)                                       |
| Computational capability | subset of HPC                                                   | superset of HTC                                                                     |
| Costs                    | lower costs per node, hence higher throughput per system budget | more expensive interconnects, high performance storage systems, specialized kernels |
| Parallelism              | While technically possible, does not scale well beyond 1 node   | Massively parallel, capable of using full machine for a single task                 |
| Homogeneity              | Very forgiving in heterogeneous nodes                           | Highly homogeneous nodes, but increasing becomes heterogeneous within node (GPGPU)  |
| MPI support              | MPI support is an afterthought                                  | MPI support is first class, MPI applications dominate                               |
| a.k.a.                   | The grid, grid computing (technically a subset of HTCs)         | Supercomputers (technically a subset of HPCs)                                       |
| Loved by                 | HEPs (CERN)                                                     | Everyone                                                                            |

### Examples of HPC & HTC in CMB data analysis

To over-simplify, the amount of memory needed in a scientific application dictates which kind of computational resources are more apt.

- Cosmoglobe style full Bayesian analysis on CMB data: all data is needed in memory. E.g. full Perlmutter system probably would be barely (in)capable for doing full Bayesian analysis on SO data
- maximal likelihood / Madam (unbiased) mapmaking: all (partial if assumptions made) data per observatory frequency is needed in memory. E.g. Planck, SO LATs, etc.
- Naïve (filter/bin, biased) mapmaking: In principle, you only need to have enough memory for a subscan.

### The NERSC problem

- See "[Mp107-u] NERSC use in 2023" email sent on Friday, Jan 20 2023 at 7:15 PM. My summary of this situation:
    - Typically [the NERSC Allocation Request Form (ERCAP)](https://www.nersc.gov/users/accounts/allocations/request-form/) is needed for a formal requests to utilize NERSC in computational research
    - CMB community is spoiled for 25 years that the application is done for all of us behind the scene, and has never been a shortage of supply (approved allocation)

    - all users are granted a generous amount of NERSC hours, based only on self-discipline
    - "a horse that harms the herd" (害群之馬) from within the CMB community using NERSC resources irresponsibly
- In the 2023 Allocation Year, $0.1\%$ of whole NERSC is allocated to SO, equivalent to a full $\sim 0.1$ PFLOPS machine.
- By my estimation SO:UK Data Centre would be of a similar order of magnitude ($\sim 0.1$ PFLOPS), where whole cluster at Blackett is about 10 times as much.

### HTC for SATs

- filter-bin (naïve mapmaking) mapmaking is suitable to be written in the map-reduce paradigm

- Riedel et al. (2019)[^1] first demonstrated adapting the filter-bin mapmaking pipelines to utilize the Open Science Grid (OSG)
- SO:UK Data Centre
    - is funded to perform SO SATs analysis,
    - located from within Blackett, a grid similar to OSG, which is an HTC,
    - funded for 8 years, a stable long term commitment to the Science Readiness of SO SATs analysis.

## Soft-launching SO:UK Data Centre v0.2.0 (What)

### What is the SO:UK Data Centre

- Physically and infrastructurally, it is located within Blackett.
- Amounts to $~10\%$ of Blackett in terms of available CPUs. Have access to most of the available nodes.
- In the way of interacting with the computational resources, we are unique in the sense that Blackett users so far are submitting their jobs very differently through DiracUI within logging into a login / submit node. We however will be logging in and use HTCondor directly.
- HTCondor itself, while an inferior job manager comparing to SLURM in handling massively parallel applications, can be viewed as SLURM-like in many aspects. However, other design choices in Blackett contributes to other differences from NERSC for example.

### Live demo

- [SO:UK Data Centre 0.2.0 documentation](https://souk-data-centre.readthedocs.io/en/latest/)
    - [1.1. Onboarding - SO:UK Data Centre 0.2.0 documentation](https://souk-data-centre.readthedocs.io/en/latest/user/onboarding/)
    - [1.2. Quick start - SO:UK Data Centre 0.2.0 documentation](https://souk-data-centre.readthedocs.io/en/latest/user/quick-start/)
    - [1.3. Running pipelines - SO:UK Data Centre 0.2.0 documentation](https://souk-data-centre.readthedocs.io/en/latest/user/pipeline/#running-pipelines)
        - [1.3.3.1. OpenMPI - SO:UK Data Centre 0.2.0 documentation](https://souk-data-centre.readthedocs.io/en/latest/user/pipeline/3-MPI-applications/1-OpenMPI/#openmpi)
        - [1.3.4.2. The grid storage system - SO:UK Data Centre 0.2.0 documentation](https://souk-data-centre.readthedocs.io/en/latest/user/pipeline/4-IO/1-grid-storage-system/)

## To be explored (How)

### How to design a workflow for a system

- To run a workflow effectively, it needs to be tailored for a system. Effectiveness can be measured in
    1. minimizing the amount of node-hours used (minimizing cost of "fair-share"),
    2. shortening the turn-around time.
- For a more capable system, it is more lenient on sub-optimality. I.e. adapting a workflow that works well at NERSC can be challenging at SO:UK Data Centre.
    - Even when a workflow works at NERSC, tailoring it for that system would makes it more "effective" as defined above.
    - E.g. for filter-bin mapmaking, you could run a big MPI job where each process is not communicating with each other.
        - This is wasting the capability of NERSC's HPC capability however.
        - It also creates more issues, such as load-balancing, that can be delegated to the job manager (scheduler) instead.
    - For NERSC, [Job Arrays](https://docs.nersc.gov/jobs/examples/#job-arrays) is a better way to launch such jobs, minimizing node-hours (because of load-balancing) and shortening the turn-around time (as the scheduler can allocate smaller jobs fitting into "cracks" earlier). This also maximize the utilization of NERSC, a cost hidden from your allocation.
- Recommended workflow: each submitted job should be "atomic", in the sense that it is the smallest piece of independent job that requires some sort of coordination within such job.
    - That means there's a lot of small jobs ($O(10,000)$ or more) you need to submit, a workflow manager is needed.
    - [Workflow managers](https://docs.nersc.gov/jobs/workflow-tools/) are independent of, often cooperate with, job managers. Example job managers are SLURM at NERSC, HTCondor in SO:UK Data Centre. Example workflow managers would be make (GNU make, makefile), snakemake, GNU Parallel, Parsl, Nextflow, of DAGMan in HTCondor.
    - Roll-your-own workflow manager are discouraged. Complexities of workflow managers:
        - Is it job-manager agnostics? Is the presence SLURM implicitly assumed?
        - How job dependencies are handled? Is the dependency graphs automatically generated and jobs submitted? E.g. after maps are made, how the next pipeline with MASTER is launched?
        - How failed jobs are handled? Do you need to keep track of corrupted output files (e.g. due to exceeding requested wall-clock time, memory available on node, etc.)? Will failed jobs be relaunched automatically?
- Caveats: while filter-bin mapmaking is well-suited for MapReduce paradigm, be careful will how you treat the data from each "map". Does it write the output to files and have the next pipeline reading it from the disks again? Beware of the explosion in intermediate disk space needed, as well as the congestion in interconnects either explicitly or implicitly. This is going to be important in co-addition of maps as well as null-split of maps where if handled not carefully would leads to data explosions and interconnect congestions.

### Documentation

Documentation available at [SO:UK Data Centre 0.2.0 documentation](https://souk-data-centre.readthedocs.io/en/latest/). How to use

- [Search](https://souk-data-centre.readthedocs.io/en/latest/search/?q=htcondor)
- Different formats are available,
    - [PDF](https://souk-data-centre.readthedocs.io/_/downloads/en/latest/pdf/) / [ePub](https://souk-data-centre.readthedocs.io/_/downloads/en/latest/epub/) / [single page HTML](https://souk-data-centre.readthedocs.io/_/downloads/en/latest/htmlzip/) from ReadTheDocs
    - [man page](https://github.com/simonsobs-uk/data-centre/releases/latest/download/soukdatacentre.1) and [plain text](https://github.com/simonsobs-uk/data-centre/releases/latest/download/soukdatacentre.txt) available from GitHub Releases
- Single file output are well-suited to Chat with LLMs:
    - [ChatGPT](https://chat.openai.com/share/91e6186b-dc26-4197-982a-815405f81627)
    - [Claude](https://shareclaude.top/c/mxnlpjh)
- Collaborate and discuss on GitHub: [simonsobs-uk/data-centre: This tracks the issues in the baseline design of the SO:UK Data Centre at Blackett](https://github.com/simonsobs-uk/data-centre)

[^1]: Riedel, Benedikt, Lincoln Bryant, John Carlstrom, Thomas Crawford, Robert W. Gardner, Nicholas Harrington, Nicholas Huang, Alexandra Rahlin, Judith Stephen, and Nathan Whitehorn. 2019. “SPT-3G Computing.” Edited by A. Forti, L. Betev, M. Litmaath, O. Smirnova, and P. Hristov. EPJ Web of Conferences 214: 03051. https://doi.org/10.1051/epjconf/201921403051.
