#!/bin/python3

# python script to check if the cubi-tk installation is present
# and is running 
# Author: Shubhada Kulkarni
# Date: 13-08-2025

import subprocess

def run_bash_command(command, capture_output=True, shell=True):
    """
    Runs a bash command and returns the output, error, and exit code.

    Args:
        command (str or list): The bash command to run.
        capture_output (bool): Whether to capture stdout and stderr.
        shell (bool): Whether to run the command through the shell.

    Returns:
        dict: Contains 'stdout', 'stderr', and 'exit_code'.
    """
    try:
        result = subprocess.run(
            command,
            shell=shell,
            capture_output=capture_output,
            text=True
        )
        return {
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "exit_code": result.returncode
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": str(e),
            "exit_code": -1
        }

# Example usage
if __name__ == "__main__":
    cmd = "cubi-tk sodar -h"
    response = run_bash_command(cmd)
    if response["exit_code"] == 0:
        print("cubi-tk installation exists and running successfully!")
        print("Output:\n", response["stdout"])
    else:
        print("Errors:\n", response["stderr"])
        print("Exit Code:", response["exit_code"])

