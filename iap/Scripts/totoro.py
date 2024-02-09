import json

odyssey_data = []

for i in range(1, 240):
    entry = {
        "a": "YoG",
        "d": "1720 × 3728",
        "n": f"totoro {i}",
        "t": f"/thumb/totoro{i}.jpeg",
        "u": f"totoro{i}.jpeg"
    }
    odyssey_data.append(entry)

with open("totoro.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
