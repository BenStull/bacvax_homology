## Overview

This set of scripts will analyze any homology of sequence window length W between an arbitrary amino acid sequence and the amino acid sequences in the human proteome.

This solution isn't very elegant due to time constraints and not wanting to create any particularly complex data structures due to what a PITA it is to deserialize json in Python. Thus, there are a couple of steps to running the analysis:

1. One time step to generate lookup tables for each sequence length W you may want to analyze

   ​	*py generate_multiple_lookup_tables.py --min 6 --max 14*

2. Run the analysis on each input sequence you are interested in

   ​	*py analyze_homology_multiple_window_lengths.py --min 6 --max 14 --sequence MLEGHESYDTENFYFREIRKNLQEVDFQWKDGEINYKEGPMTHK*

**This will create one output file per window length (e.g. *results_6.csv*..*results_14.csv*) in the *results* subdirectory (previous results will be overwritten)** 



## Full Description of Output

| Column                            | Description                                                  |
| --------------------------------- | ------------------------------------------------------------ |
| Matched Sequence                  | The subsequence of the input sequence that matched a sequence in the human genome. This length will be the same as the window length requested |
| Index in Input Sequence (0-based) | The index where the matched sequence can be found in the input sequence |
| Entry                             | The entry in the human proteome where the match was found (this corresponds to the "Entry name" column in the Human_Proteome_20K_proteins.csv file, sans the '_HUMAN' suffix) |
| Index in Entry Sequence (0-based) | The index where the matched sequence can be found in the 'Sequence' column of the entry in the Human_Proteome_20K_proteins.csv file |



Example: providing an amino acid sequence of *MLEGHESYDTENFYFREIRKNLQEVDFQWKDGEINYKEGPMTHK* as input and a sequence window match length of W=6 will provide results with the following (abridged):

| Matched Sequence | Index in Input Sequence (0-based) | Entry | Index in Entry Sequence (0-based) |
| ---------------- | --------------------------------- | ----- | --------------------------------- |
| MLEGHE           | 0                                 | ZN841 | 0                                 |
| LEGHES           | 1                                 | ZN841 | 1                                 |
| LEGHES           | 1                                 | CIAO1 | 189                               |
| EGHESY           | 2                                 | ZN841 | 2                                 |
| GHESYD           | 3                                 | ZN841 | 3                                 |

The first row of these results can be read as: "I matched the sequence *MLEGHE*, which is at index 0 of the sequence you asked me to analyze, at position 0 of human proteome entry *ZN841_HUMAN*"



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

## License

MIT License

Copyright (c) 2022 Ben Stull

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
