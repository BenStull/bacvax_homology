import argparse
import json
from re import sub
import sys
import csv
import json
import os
from bacvax_homology_common import *

parser = argparse.ArgumentParser(description="BacVax Homology Lookup Table Generator")
parser.add_argument("-w", "--window", help="Window size of the lookup table (e.g. 5 to create a lookup table that can match at most a 5Aa sequence)", type=int)
parser.add_argument("-i", "--input", help="Input CSV file with the human proteome. This is included with the BacVax Homology package in the 'data' directory")
parser.add_argument("-o", "--output", help="Output file name. By default. the lookup table will be output to the 'data' subdirectory of the current working directory and be named 'lookup_N.json' where N is the window length (e.g. ./data/lookup_6.json")
parser.add_argument("-t", "--test", help="Run validation tests on output (not needed unless making changes to the script", action="store_true")

args=parser.parse_args()

window: int=args.window
input: str=args.input
output: str=args.output
test: bool=args.test

lookup=lookup_table()

if (window == None):
    parser.print_help()
    sys.exit(0)

if (input == None):
    input=f"./data/Human_Proteome_20K_proteins.csv"

if not os.path.exists(input):
    print(f"Unable to find input file {os.path.abspath(input)}")
    sys.exit(0)

if (output == None):
    output=f"./data/lookup_{window}.json"

# Test data
entry_A0A0A0MT89_sequence_matches=0

### Read in the CSV
with open(input, 'r') as input_csvfile:
    input_lines = csv.reader(input_csvfile)
    next(input_lines) # Skip header
    for line in input_lines:
        entry=line[1].replace("_HUMAN", "")
        sequence=line[5]
        end_range=len(sequence)-window+1
        if end_range <= 0:
            print(f"Entry {entry} with sequence '{sequence}' has length less than {window}...skipping")
            continue
        processed=0
        for idx in range(0, end_range):
            lookup.add(lookup_sequence=sequence[idx:idx+window], sequence_match=sequence_match(entry=entry, offset=idx))
            processed=idx+1
        if entry=='A0A0A0MT89':
            entry_A0A0A0MT89_sequence_matches=processed

        print(f"Registered {processed} sequences of length {window} in {entry}")

if test:
    print("Running validation tests...")
    entry_A0A0A0MT89_length=12
    entry_A0A0A0MT89_expected_sequence_matches=entry_A0A0A0MT89_length-window+1
    print(f"Asserting that entry A0A0A0MT89 has {entry_A0A0A0MT89_expected_sequence_matches} sequences")
    if entry_A0A0A0MT89_sequence_matches != entry_A0A0A0MT89_expected_sequence_matches:
        print(f"FAILED: Found {entry_A0A0A0MT89_sequence_matches} matches for A0A0A0MT89")
    else:
        print(f"SUCCESS: Found {entry_A0A0A0MT89_sequence_matches} matches for A0A0A0MT89")

print(f"Writing lookup table to {output}...")

if os.path.exists(output):
    os.remove(output)

with open(output, 'w') as out:
    out.write(lookup.toJSON())

print(f"Successfully output lookup table to {output}")
print("Hold tight - cleaning up...")
