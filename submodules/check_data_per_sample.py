#!/bin/python3

# python script to check per sample if the data is present
# and if so, arrange it in a proper form to upload to SODAR
# Author: Shubhada Kulkarni
# Date: 14-08-2025

# This script takes as an input the sample names list from the previous step

import sys
import os, os.path
from glob import glob
import re

def is_illumina_fastq(filename):
    # function to check if fastq filenames have a proper naming convention 
    # (if this is not followed, the links per sample in SODAR wont appear)
    '''
    Args:
        fastq filename in current format
    Returns:
        boolean if filename is in a proper format or not
    '''
    pattern = r"^([\w\-]+)_S\d+_L\d{3}_R[12]_\d{3}\.fastq\.gz$"
    print(filename, re.match(pattern, filename) is not None)
    return re.match(pattern, filename) is not None

is_illumina_fastq("DB_30_miRNA.fastq.gz")
is_illumina_fastq("MySample_S1_L001_R1_001.fastq.gz")
is_illumina_fastq("MySample_S1_L001_R1_001.fq.gz")
is_illumina_fastq("Sample_S1_L001_R3_001.fastq.gz")

def find_data(samples, data_dir):
    # function that checks if the data for each sample is present or not
    # and if necessary, adjusts the filenames
    '''
    Args:
        sample: sample name
        data_dir: temp downloaded data from CardioCloud where the data per sample will be checked
    Returns:
        Flag if all good or not to proceed (return 0 for all good; 1 for issues and list of samples for which no data was found if this is the case)
    '''
    try:
        nofiles = []
        for each in samples:
            # print(each)
            list_files = glob(data_dir+"/"+each+"*", recursive=True)
            # print(list_files)
            if len(list_files) == 0:
                print(f"Warning!! No files found for sample: {each}")
                nofiles.append(each)
            else:
                print(f"Files found for sample: , {each}, {list_files}")

                ## check if fastq files and if so, check if they follow the file convention
                if 

        if len(nofiles) == 0:
            return(0)
        else:
            return(nofiles)
    except Exception as e:
        print("Prolems reading in the sample names.")
        print(e)
        return(1)

find_data(['DB_32_miRNA'], "/home/skulkarni/workflow/temp_testing/")
# find_data(['DB_30_miRNA'], "/home/skulkarni/workflow/temp_testing/")
