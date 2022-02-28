import os
import argparse
import csv
from bacvax_homology_common import *

parser = argparse.ArgumentParser(description="BacVax Homology Sequence Analyzer (Multiple Lengths)\r\nThis will call the analyze_homology.py script multiple times for different window sizes with default parameters except for outputting results to CSV files")
parser.add_argument("--min", help="Smallest window size sequence you want to match", type=int, required=True)
parser.add_argument("--max", help="Largest window size sequence you want to match", type=int, required=True)
parser.add_argument("-s", "--sequence", help="Smallest window size sequence you want to match", type=str, required=True)

args = parser.parse_args()

for window_len in range(args.min, args.max+1):
    os.system(f"python analyze_homology.py -w {window_len} -o ./results/results_{window_len}.csv -s {args.sequence}")

results: list[result]=[]

print(f"Coalescing results and outputting to {os.path.abspath('./results/results_{args.min}_{args.max}.csv')}")

## Coalesce the results
for window_len in range(args.max, args.min-1, -1):
    with open(f"./results/results_{window_len}.csv", 'r') as input_csvfile:
        input_lines = csv.reader(input_csvfile)
        next(input_lines) # Skip header
        for line in input_lines:
            matched_sequence=line[0]
            entry=line[2]
            is_submatch=False
            for existing_result in results:
                if entry==existing_result.entry and matched_sequence in existing_result.matched_sequence:
                    is_submatch=True
                    break
            if not is_submatch:
                results.append(result(entry=entry, matched_sequence=matched_sequence, idx_input_sequence=line[1], idx_entry_sequence=line[3]))

write_results_to_csv(results, f"./results/results_{args.min}_{args.max}.csv")