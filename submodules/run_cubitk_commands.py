#!/bin/python3

# python script to run cubi-tk create landing zone, upload the data, validate and move the data
# and is running 
# Author: Shubhada Kulkarni
# Date: 15-08-2025

# eveything needed for this script - project ID on SODAR, data folder, sample names, other settings for SODAR?

import sys
import subprocess
import json

def create_landing_zone(project_id, capture_output=True, shell=True):
    """
    Creates a cubi-tk landing zone

    Args:
        project_id (str): UUID for the project on SODAR

    Returns:
        Will return a UUID for landing zone that has been created
    """
    try:
        command = 'cubi-tk sodar landing-zone-create --sodar-url "https://sodar-test.internal/" --sodar-api-token "d1f108f3576bae3741e769c589189da7821d466dd77a3d0ec1593283f941b3b1" ' + project_id
        result = subprocess.run(
            command,
            shell=shell,
            capture_output=capture_output,
            text=True
        )
        if result.returncode == 0:
            print("Successfully created a landing zone.")
            # convert the json output to dictionary to fetch the landing zone uuid
            json_acceptable_string = result.stdout.strip()
            out_dict = json.loads(json_acceptable_string)
            lz_uuid = out_dict['sodar_uuid']
            print(f"Created landing zone with UUID: {lz_uuid}")
            return(lz_uuid)
        else:
            print("Landing zone could not be created. Please check:\n", result.stderr.strip())
            return(None)
    except Exception as e:
        return(None)

create_landing_zone("aa9c3f41-756c-4206-8e02-e5c2f2c2dcc2")
