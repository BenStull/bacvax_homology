## Output

| Column                            | Description                                                  |
| --------------------------------- | ------------------------------------------------------------ |
| Matched Sequence                  | The subsequence of the input sequence that matched a sequence in the human genome. This length will be the same as the window length requested |
| Index in Input Sequence (0-based) | The index where the matched sequence can be found in the input sequence |
| Entry                             | The entry in the human proteome where the match was found (this corresponds to the "Entry name" column in the Human_Proteome_20K_proteins.csv file, sans the '_HUMAN' suffix) |
| Index in Entry Sequence (0-based) | The index where the matched sequence can be found in the 'Sequence' column of the entry in the Human_Proteome_20K_proteins.csv file |



## Environment Install Instructions

#### 1. Install Python

Install the latest version of python 3.xx from  [Download Python | Python.org](https://www.python.org/downloads/)

Ensure that the path to python is added to your local %PATH% environment variable so you can type "py" from anywhere in a command prompt and it will invoke python

#### 2. Install bacvax_homology

Download the latest release of bacvax_homology and extract it to a local directory (henceforth referred to as %bh_install%)

#### 4. Open a Command Prompt and navigate to your %bh_install% dir

#### 5. Install PIP

Type *py -m ensurepip --upgrade*

#### 6. Install python packages that the BacVax Homology python scripts rely on

Type *pip install -r requirements.txt*

#### 7. Generate lookup tables for the set of window lengths you want to match against

From your %bh_install% dir, run *py generate_multiple_lookup_tables.py -h* to get instructions for generating a lookup table

This script will generate a lookup table for each sequence window length *w* within [min, max] that you want to match against. The lookup tables (one per window length) will be output to the *data* subdirectory

Example command to generate a lookup table if you want to match homologous sequences of window lengths *[min=6,max=14]*:

*py generate_multiple_lookup_tables.py --min 8 --max 14*

The lookup tables are each several hundred megabytes, so only generate lookup tables for window lengths you want to check against. These lookup tables are independent of the sequence you want to check against the human genome - you only need to run this step once per window length you're interested in checking.

#### 8. Check your protein sequence for matches

Now that you have your lookup table(s), you can check your sequence. Example to get all matches with a sequence window of 5:

*py analyze_homology.py -w 5 -s DIQNNIDNIYDLAQQQDRHAYDIQNLAKSAYS -o match_5.csv*

This will take all sequences of length 5 within the sequence *DIQNNIDNIYDLAQQQDRHAYDIQNLAKSAYS* and check for matches. Results will be output to the file "match_5.csv" in the local directory

Example to get all matches for sequence windows of length 8-14:

*py analyze_homology_multiple_window_lengths.py --min 8 --max 14 --sequence DIQNNIDNIYDLAQQQDRHAYDIQNLAKSAYS

This will create one output file per window length (*results_8.csv*..*results_14.csv*) in the *results* subdirectory (previous results will be overwritten) 

