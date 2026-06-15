import json
def load_users():
    with open('data/users.json') as f:
        return json.load(f)