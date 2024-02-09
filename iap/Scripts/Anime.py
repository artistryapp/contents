import json

odyssey_data = []

for i in range(1, 198):
    entry = {
        "a": "YoG",
        "d": "1720 × 3728",
        "n": f"Scenery {i}",
        "t": f"/thumb/Anime_Scenery_{i}.jpg",
        "u": f"Anime_Scenery_{i}.jpg"
    }
    odyssey_data.append(entry)

with open("AnimeScenery.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
