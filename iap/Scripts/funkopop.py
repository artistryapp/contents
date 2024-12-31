import json

odyssey_data = []

for i in range(139, 203):
    entry = {
       "a": "YoG",
        "d": "1472x3200",
        "n": str(i),
        "t": "/thumbs/FunkoPOP_{}.jpg".format(i),
        "u": "FunkoPOP_{}.jpg".format(i)
    }
    odyssey_data.append(entry)

with open("FunkoPOP.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
