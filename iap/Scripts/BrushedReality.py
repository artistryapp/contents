import json

odyssey_data = []

for i in range(107, 141):
    entry = {
       "a": "YoG",
        "d": "1472x3200",
        "n": str(i),
        "t": "/thumbs/brushedReality_00{}.jpg".format(i),
        "u": "brushedReality_00{}.jpg".format(i)
    }
    odyssey_data.append(entry)

with open("brushedReality.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
