import json

with open("JsonData.json",'r') as f:
    data=json.load(f)
    print(data)