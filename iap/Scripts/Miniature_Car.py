import json

odyssey_data = []

for i in range(1, 279):
    entry = {
        "a": "YoG",
        "d": "4096 × 5438",
        "n": f"Miniature Car {i}",
        "t": f"/thumbs/MiniatureCar_{i}.jpg",
        "u": f"MiniatureCar_{i}.jpg"
    }
    odyssey_data.append(entry)

with open("MiniatureCars.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
