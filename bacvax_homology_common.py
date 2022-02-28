import json
from msilib import sequence
import os
import csv

class sequence_match(object):
    def __init__(self, entry: str, offset: int):
        self.e=entry
        self.o=offset

    e: str
    o: int

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class lookup_table(dict):
    def fromJSON(self, json_str: str):
        obj = json.loads(json_str)
        for lookup_sequence in obj:
            for match in obj[lookup_sequence]:
                self.add(lookup_sequence, sequence_match(entry=match['e'], offset=match['o']))

    def add(self, lookup_sequence: str, sequence_match: sequence_match):
        if not lookup_sequence in self:
            self[lookup_sequence]=[]
        self[lookup_sequence].append(sequence_match)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class result(object):
    def __init__(self, entry: str, matched_sequence: str, idx_input_sequence: int, idx_entry_sequence: int):
        self.entry=entry
        self.matched_sequence=matched_sequence
        self.idx_input_sequence=idx_input_sequence
        self.idx_entry_sequence=idx_entry_sequence
    entry: str
    matched_sequence: str
    idx_input_sequence: int
    idx_entry_sequence: int

def write_results_to_csv(results: list[result], outputfile):
    if len(results) > 0 and not outputfile==None:
        print(f"Writing results to {os.path.abspath(outputfile)}...")
        if os.path.exists(outputfile):
            os.remove(outputfile)
        with open(outputfile, 'w', newline='') as csvfile:
            writer=csv.DictWriter(csvfile, fieldnames=['Matched Sequence', 'Index in Input Sequence (0-based)', 'Entry', 'Index in Entry Sequence (0-based)'])
            writer.writeheader()
            for a_result in results:
                writer.writerow({'Matched Sequence': a_result.matched_sequence, 'Index in Input Sequence (0-based)': a_result.idx_input_sequence, 'Entry': a_result.entry, 'Index in Entry Sequence (0-based)': a_result.idx_entry_sequence })
