#!/bin/bash

# main script that uploads the data to sodar
# Author: Shubhada Kulkarni
# Date: 13-08-2025
# Email: shubhada.kulkarni@uni-heidelberg.de


########################## Modules ##########################
# Loading required modules
import argparse
import os.path
import sys

from submodules import check_cubitk_installation as check


########################## Arguments ##########################
parser = argparse.ArgumentParser(
        description="SODAR upload wrapper script")

parser = argparse.ArgumentParser(
                    prog='sodar_upload',
                    description='This program performs data upload to SODAR platform',
                    epilog='Please provide all required arguments')

# Named arguments
parser.add_argument(
        "--input_folder",
        required=True,
        action="store_true",
        help="Input CardioCloud folder that will be rcloned."
    )

parser.add_argument("-l",
        "--local",
        dest="local",
        help="If the data should be fetched from local folders, turn this flag on",
        default=False,
        action='store_true'
    )

parser.add_argument(
        "--uuid",
        type=str,
        required=True,
        help="SODAR Project ID where this data needs to be uploaded."
    )

parser.add_argument(
        "--verbose",
        action="store_true",
        default=True,
        help="Enable verbose output"
    )

args = parser.parse_args()
print(args)

# Example usage
if args.verbose:
    print("Verbose mode enabled")
print(f"Input file: {args.input}")
print(f"Output file: {args.output}")

########################## cubi-tk installation check ##########################
cmd = "cubi-tk sodar -h"
response_check = check.run_bash_command(cmd)

if response_check["exit_code"] == 0:
    print("cubi-tk installation exists and running successfully!")
    print("Output:\n", response_check["stdout"])
else:
    print("Errors:\n", response_check["stderr"])
    print("Exit Code:", response_check["exit_code"])

########################## cubi-tk installation check ##########################
