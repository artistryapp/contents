import json
import random

odyssey_data = []

for i in range(1, 124):
    entry = {
        "a": "YoG",
        "d": "4096 × 5438",
        "n": f"Funko {i}",
        "t": f"/thumbs/FunkoPOP_{i}.jpg",
        "u": f"FunkoPOP_{i}.jpg"
    }
    odyssey_data.append(entry)

# Shuffle the list of entries
random.shuffle(odyssey_data)

with open("FunkoPOP.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
