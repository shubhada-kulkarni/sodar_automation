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
from submodules import check_cardiocloud_data as rclone


########################## Arguments ##########################
#parser = argparse.ArgumentParser(
#        description="SODAR upload wrapper script")

parser = argparse.ArgumentParser(
                    prog='sodar_upload',
                    description='This program performs data upload to SODAR platform',
                    epilog='Please provide all required arguments',
                    exit_on_error=False)

# Named arguments
parser.add_argument("-v",
        "--verbose",
        action="store_true",
        default=False,
        help="Enable verbose output")

parser.add_argument("-i",
        "--input_folder",
        required=False,
        type=str,
        help="Input CardioCloud folder that will be rcloned.")

parser.add_argument("-o",
        "--uuid",
        type=str,
        required=True,
        help="SODAR Project ID where this data needs to be uploaded.\nPlease go to SODAR, create category/project and copy the UUID here.")

parser.add_argument("-l",
        "--local",
        dest="local",
        help="If the data should be fetched from local folders, turn this flag on",
        default=False)

parser.add_argument("-t",
        "--temp",
        type=str,
        required=False,
        default="/home/skulkarni/temp_sodar/",
        help="Temp folder name where data from CardioCloud will be stored and removed after transfer.")

args = parser.parse_args()
print(args)

# Example usage
if args.verbose:
    print("Verbose mode enabled")
print(f"#Running SODAR project upload! Please check the following parameters:")
print(f"#Input folder: {args.input_folder}")
print(f"#Output project UUID: {args.uuid}")
print(f"#Temporary folder where files from CardioCloud will be stored: {args.temp}")


########################## cubi-tk installation check ##########################
#  check if cubi-tk is installed and is running
cmd = "cubi-tk sodar -h"
response_check = check.run_bash_command(cmd)

if response_check["exit_code"] == 0:
    print("#cubi-tk installation exists and running successfully!")
    #print("Output:\n", response_check["stdout"])
else:
    print("Looks like there are some problem with installations of cubi-tk. Please check!")
    print("Errors:\n", response_check["stderr"])
    print("Exit Code:", response_check["exit_code"])

########################## CardioCloud folder download  ##########################
# check if the folder on CardioCloud exists and if so, rclone it to a temp directory
response_rclone = rclone.check_cardiocloud_data(args.input_folder, args.temp) 
if response_rclone['exit_code'] == 0:
    print("#Input data folder exists on CardioCloud. Proceeding to download.")
    print("Data details\n", response_rclone['stdout'])
    response_rclone_copy = rclone.download_cardiocloud_data(args.input_folder, args.temp)
    if response_rclone_copy['exit_code'] == 0:
        print("CardioCloud data folder downloaded into", args.temp)
    else:
        print("Errors downloading data from CardioCloud", response_rclone_copy['stderr'])

else:
    print("*CardioCloud folder not found. Please check and re-run!")
    print(response_rclone['stderr'])
    sys.exit("Exiting because input folder not found on CardioCloud")
#print(response_rclone)
#print(response_rclone_copy)





