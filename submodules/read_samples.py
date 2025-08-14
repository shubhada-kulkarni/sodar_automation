#!/bin/python3

# python script to read the sample names from the ISA-TAB sample template.
# Author: Shubhada Kulkarni
# Date: 14-08-2025

# This script takes as an input the study file from ISA-TAB template.

import sys
import os, os.path

def read_isa_study_file(studyfile):
    # function that first checks if the study file is present 
    # and if its there, reads this file and returns the sample names for
    # this project
    #
    '''
    Args:
        Study file from ISA-TAB template of the project (ideally filled in by the user)
    Returns:
        List of sample names
    '''
    if not os.path.isfile(studyfile):
        print("*The given study file with sample names does not exist. Exiting!")
        sys.exit()

    else:
        try:
            samples = [x.split('\t')[0] for x in open(studyfile).readlines()]
            for each in samples:
                if "Source" in each:
                    samples.remove(each)
            print(samples)
            return(samples)
        except Exception as e:
            print("Problems in reading the sample file")
            print(e)
            return(NULL)

read_isa_study_file("/home/skulkarni/workflow/test_template/s_{{cookiecutter.s_file_name}}.txt")
