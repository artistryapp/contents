import json

data = []

for i in range(101, 0, -1):
    entry = {
        "a": "YoG",
        "d": "1472×3200",
        "n": f"name {i}",
        "t": f"artistry_{i}.jpg",
        "u": f"artistry_{i}.jpeg"
    }
    data.append(entry)

with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=2)
