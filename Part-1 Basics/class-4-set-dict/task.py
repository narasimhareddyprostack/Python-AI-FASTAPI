import json

data = {'eid': 101, 'avail': True}

# Convert dictionary to JSON string
json_data = json.dumps(data)

print(json_data)  # Output: {"eid": 101, "avail": true}
