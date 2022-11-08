import json

def to_json(user_dict):
    return json.dumps(user_dict)

def from_json(user_string):
    return json.loads(user_string)
