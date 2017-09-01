#!/usr/bin/python

import os
import sys
import argparse
import re

"""

This script changes Illumina file prefixes to the sample ids from the table.

usage: prefix2id.py [-h] -n NAMES -d DIR [-l LANE]

Rename multiple files in the folder changing prefixes to ids. E.g., Illumina's
prefixes like 01_S01_L001...

optional arguments:
  -h, --help            show this help message and exit
  -n NAMES, --names NAMES
                        (required) The name of the file with sample IDs. There
                        are 2 columns: in the left prefixes and in the right
                        sample names
  -d DIR, --dir DIR     (required) The folder where you want to rename files
  -l LANE, --lane LANE  The Illumina lane number

"""

# get arguments
parser = argparse.ArgumentParser(description="Rename multiple files in the folder changing prefixes to ids. Eg, Illumina's prefixes like 01_S01_L001...")
parser.add_argument("-n","--names", help="(required) The name of the file with sample IDs. There are 2 columns: in the left prefixes and in the right sample names", type=str, required=True)
parser.add_argument("-d","--dir", help="(required) The folder where you want to rename files", type=str, required=True)
parser.add_argument("-l","--lane", help="The Illumina lane number", type=str, default='L00')
args = parser.parse_args()



# make a dictionary of names
filenames = {}

with open(args.names) as f:
    for line in f:
        line=line.replace('(', '_').replace(' ','_').replace(')', '').replace('__','_')
        line=line.strip()
        t = line.split()
        filenames[t[0]] = t[1]

print("The name dictionary is complete\n")
f.close()


# change a directory
os.chdir(args.dir)


# rename files
for file in os.listdir('.'):
    match_name=re.search(r"^([0-9]+)_S[0-9]+_" + args.lane, file)             # change it if other prefixes
    if match_name:
        id=match_name.group(1)
        old_name = id + '_S' + id             # change it if other prefixes
        new_name = filenames[id] + '_S' + id
        os.rename(file, file.replace(old_name, new_name))
        print(file + " ... done")
    else:
        print('Some problems with file ' + file)

print("Done!\n")
