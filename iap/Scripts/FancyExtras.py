import json

odyssey_data = []

for i in range(1, 25):
    entry = {
        "a": "YoG",
        "d": "1284 × 2778",
        "n": f"Extras {i}",
        "t": f"/thumbs/HumanCompanion_{i}.jpg",
        "u": f"HumanCompanion_{i}.jpg"
    }
    odyssey_data.append(entry)

with open("fancyAnimalsEx.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
