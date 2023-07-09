import json

odyssey_data = []

for i in range(1, 176):
    entry = {
        "a": "YoG",
        "d": "1472 × 3200",
        "n": f"Odyssey {i}",
        "t": f"/thumbs/Odyssey_{i}.jpeg",
        "u": f"Odyssey_{i}.jpeg"
    }
    odyssey_data.append(entry)

with open("odyssey_data.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
