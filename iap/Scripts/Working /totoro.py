import json
import random

odyssey_data = []

for i in range(1, 96):
    entry = {
        "a": "YoG",
        "d": "1720x3728",
        "n": f"Funko {i}",
        "t": f"/thumb/totoro{i}.jpeg",
        "u": f"totoro{i}.jpeg"
    }
    odyssey_data.append(entry)

# Shuffle the list of entries
random.shuffle(odyssey_data)

with open("totoro.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
