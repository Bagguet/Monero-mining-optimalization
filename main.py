import json

with open("info.json", "r") as f:
    info = json.load(f)

print(info)