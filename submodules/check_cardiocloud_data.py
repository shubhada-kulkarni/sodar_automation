#!/bin/python3

# python script to check if the cubi-tk installation is present
# and is running 
# Author: Shubhada Kulkarni
# Date: 13-08-2025

import subprocess

def check_cardiocloud_data(cc_folder, capture_output=True, shell=True):
    """
    Runs a bash command and returns the output, error, and exit code.

    Args:
        command (str or list): The bash command to run.
        capture_output (bool): Whether to capture stdout and stderr.
        shell (bool): Whether to run the command through the shell.

    Returns:
        dict: Contains 'stdout', 'stderr', and 'exit_code'.
    """
    # using the input folder name, first check the size of the folder that will be copied.
    cmd = "rclone size crc1550:" + cc_folder + "/"
    try:
        result = subprocess.run(
            cmd,
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
    #response = check_cardiocloud_data("CRC1550-B10_data/")
    response = check_cardiocloud_data("Multiome_Submission")
    if response["exit_code"] == 0:
        print("Data folder found on CardioCloud")
        print("Output:\n", response["stdout"])
    else:
        print("Data folder not found on CardioCloud. Please provide the correct folder name!")
        print("Errors:\n", response["stderr"])
        print("Exit Code:", response["exit_code"])

