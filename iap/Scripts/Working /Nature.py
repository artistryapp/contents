import json
import random

odyssey_data = []

for i in range(1, 175):
    entry = {
        "a": "YoG",
        "d": "1720x3728",
        "n": f"Odyssey {i}",
        "t": f"/thumb/Odyssey_{i}.jpg",
        "u": f"Odyssey_{i}.jpg"
    }
    odyssey_data.append(entry)

# Shuffle the list of entries
random.shuffle(odyssey_data)

with open("naturesOdyssey.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
