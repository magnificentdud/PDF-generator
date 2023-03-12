import json

with open('user_defined_laayout.json','r') as f:
    json_data = json.load(f)

for k,v in json_data.items():
    for elem in v:
        for attr_name, value in elem.items():
            print(attr_name, value)
