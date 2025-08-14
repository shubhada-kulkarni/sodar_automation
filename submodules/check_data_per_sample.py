#!/bin/python3

# python script to check per sample if the data is present
# and if so, arrange it in a proper form to upload to SODAR
# Author: Shubhada Kulkarni
# Date: 14-08-2025

# This script takes as an input the sample names list from the previous step

import sys
import os, os.path
from glob import glob

def find_data(samples, data_dir):
    # function that checks if the data for each sample is present or not
    # and if necessary, adjusts the filenames
    '''
    Args:
        sample: sample name
        data_dir: temp downloaded data from CardioCloud where the data per sample will be checked
    Returns:
        Flag if all good or not to proceed (return 0 for all good; 1 for issues)
    '''
    try:
        for each in samples:
            print(each)
            list_files = glob(data_dir+"/"+each+"*", recursive=True)
            print(list_files)
            return(0)
    except Exception as e:
        print("Problems in reading the sample file")
        print(e)
        return(1)

find_data(['DB_32_miRNA'], "/home/skulkarni/workflow/temp_testing/")
