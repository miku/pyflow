
import json

class Processor:
    
    def __init__(self, records):
        """
        (1) No need for duplication (data, loaded) 
        """
        self.records = records
    
    def filter_by_key(self, key):
        """
        (2) A basic filter by key.
        (3) Can reuse already set records
        (4) Make it clearer, that we check for existence (a set would be even clearer, but may distort the output)
        """
        result = []
        for record in self.records:
            if any(key in record for record in result):
                continue
            result.append(record)
        return result
     
    def run(self):
        for record in self.filter_by_key('a'):
            print(record)
            
    

# (5) Loading becomes a bit more independent (could be from any format).
data = '[{"a": 1}, {"b": 2}, {"c": 3}, {"a": 4}, {"b": 5}]'
records = json.loads(data)
processor = Processor(records=records)
for record in processor.filter_by_key('a'):
    print(record)