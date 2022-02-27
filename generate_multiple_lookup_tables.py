import os
import argparse
import subprocess

parser = argparse.ArgumentParser(description="BacVax Homology Lookup Table Generator (Multiple Tables Edition)\r\nThis will call the generate_lookup_table.py script multiple times with default parameters")
parser.add_argument("--min", help="Smallest window size lookup table you want to generate", type=int, required=True)
parser.add_argument("--max", help="Largest window size lookup table you want to generate", type=int, required=True)

args = parser.parse_args()

for window_len in range(args.min, args.max+1):
    os.system(f"python generate_lookup_table.py -w {window_len}")
