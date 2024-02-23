import json
import random

odyssey_data = []

for i in range(1, 197):
    entry = {
        "a": "YoG",
        "d": "1720x3728",
        "n": f"Scenery {i}",
        "t": f"/thumb/Anime_Scenery_{i}.jpg",
        "u": f"Anime_Scenery_{i}.jpg"
    }
    odyssey_data.append(entry)

# Shuffle the list of entries
random.shuffle(odyssey_data)

with open("animeScenery.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
