import os
import argparse
import subprocess

parser = argparse.ArgumentParser(description="BacVax Homology Sequence Analyzer (Multiple Lengths)\r\nThis will call the analyze_homology.py script multiple times for different window sizes with default parameters except for outputting results to CSV files")
parser.add_argument("--min", help="Smallest window size sequence you want to match", type=int, required=True)
parser.add_argument("--max", help="Largest window size sequence you want to match", type=int, required=True)
parser.add_argument("-s", "--sequence", help="Smallest window size sequence you want to match", type=str, required=True)

args = parser.parse_args()

for window_len in range(args.min, args.max+1):
    os.system(f"python analyze_homology.py -w {window_len} -o ./results/results_{window_len}.csv -s {args.sequence}")
