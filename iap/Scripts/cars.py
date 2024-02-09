import json

odyssey_data = []

for i in range(1, 279):
    entry = {
        "a": "YoG",
        "d": "1720 × 3728",
        "n": f"Miniature Car {i}",
        "t": f"/thumb/car_{i}.jpg",
        "u": f"car_{i}.jpg"
    }
    odyssey_data.append(entry)

with open("cars.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
