
"""
The following code has some issues, find them and try to correct them.

Note: This class does not have tests (no need to add any for the moment).
However, real refactoring should be done against tested code.
"""

import json

class Processor:
    
    def __init__(self, data=None, lookup=None):
        self.data = data
        
    def load(self):
        self.loaded = json.loads(self.data)
    
    def filter_by_a(self, records):
        result = []
        for record in records:
            if 'a' in record:
                for value in result:
                    if 'a' in value:
                        break
                else:
                    result.append(record)
        return result

    def filter_by_b(self, records):
        result = []
        for record in records:
            if 'b' in record:
                for value in result:
                    if 'b' in value:
                        break
                else:
                    result.append(record)
        return result
                 
    

data = '[{"a": 1}, {"b": 2}, {"c": 3}, {"a": 4}, {"b": 5}]'
processor = Processor(data=data)
processor.load()
for record in processor.filter_by_a(processor.loaded):
    print(record)