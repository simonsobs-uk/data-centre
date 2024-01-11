import subprocess


def get_hostnames() -> list[str]:
    """Get hostnames of all machines.

    Similar to this command:

        run sudo condor_status -format "%s\\n" Machine | sort -u

    """
    cmd = ["sudo", "condor_status", "-format", "%s\n", "Machine"]
    result = subprocess.run(cmd, text=True, check=True, capture_output=True)
    return sorted(set(i for i in result.stdout.split("\n") if i))
