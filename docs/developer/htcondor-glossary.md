{#htcondor-glossary}
# HTCondor Glossary

ClassAd
: ClassAd stands for "Classified Advertisement." It's a flexible and expressive language used by HTCondor for representing jobs, machines, and other resources. ClassAds are similar to attribute-value pairs, and they're used to match jobs with appropriate resources.

Scheduler
: The component in HTCondor that queues and manages users' job submissions. It finds appropriate matches for the jobs in the queue using the ClassAd system.

Startd (Start Daemon)
: This is the daemon running on the worker node that advertises the node's resources and capabilities. It's responsible for executing and managing jobs on the node.

Negotiator
: Part of the central manager services, it is responsible for making match decisions, pairing submitted jobs with suitable execution resources.

Worker Nodes (or Execute Nodes)
: The computational resources or machines where the jobs are executed. Each worker node runs a startd process.

Submit Node
: The machine or location from which jobs are submitted into the HTCondor system. The scheduler runs on this node.

Central Manager
: The central authority in an HTCondor pool that hosts the Negotiator and the Collector services. It’s essential for resource matchmaking and information gathering.

Collector
: A service running on the Central Manager that gathers ClassAd information from other daemons (like startd and schedd) across the pool.

Condor Pool
: A collection of machines working under a single HTCondor system. This includes the Central Manager, Worker Nodes, and potentially multiple submit nodes.

Universe
: In HTCondor, a Universe is a specific execution environment for a job. Examples include the Vanilla Universe, Parallel Universe, and Docker Universe. The chosen Universe determines how a job is executed and what features are available to it.

Checkpointing
: A feature that allows jobs to be paused and resumed. This is especially useful if a job gets preempted or if the machine it's running on goes down.

Preemption
: The act of suspending or stopping a currently running job to free up resources for another job that has higher priority or better matches the resources.

Rank
: An expression in the ClassAd system that indicates a preference for a match. For example, a job might rank execution machines by available memory, favoring matches with more memory.

Requirements
: Expressions in the ClassAd system that must be satisfied for a match to occur. If a job's requirements do not match the attributes of a machine, then the job will not be sent to that machine.

Dedicated Scheduling
: In the HTCondor Parallel Universe, "dedicated" scheduling refers to the process by which certain compute nodes (machines) are reserved exclusively for running parallel jobs. Such a setup ensures that parallel jobs, like MPI jobs, have consistent and predictable communication between the nodes without interference from other non-parallel jobs. Dedicated scheduling is advantageous for jobs that require tight inter-process communication or a specific arrangement of nodes. When machines are part of the dedicated scheduler, they won't execute other tasks outside of the designated parallel jobs.
