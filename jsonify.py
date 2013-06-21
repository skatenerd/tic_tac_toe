import json

class JsonPrinter(object):
    
    def display(self,x):
        return json.dumps(x)
