import json
from msilib import sequence

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

