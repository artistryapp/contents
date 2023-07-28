import json

odyssey_data = []

for i in range(1, 257):
    entry = {
        "a": "YoG",
        "d": "1284 × 2778",
        "n": f"Animal {i}",
        "t": f"/thumbs/ChibiAnimals{i}.jpg",
        "u": f"ChibiAnimals{i}.jpg"
    }
    odyssey_data.append(entry)

with open("chibistyleAnimals.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
