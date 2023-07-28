import json

odyssey_data = []

for i in range(1, 44):
    entry = {
        "a": "YoG",
        "d": "1284 × 2778",
        "n": f"Extras {i}",
        "t": f"/thumbs/ChibiExtras{i}.jpg",
        "u": f"ChibiExtras{i}.jpg"
    }
    odyssey_data.append(entry)

with open("chibistyleAnimalsExtras.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
