import json

odyssey_data = []

for i in range(82, 144):
    entry = {
       "a": "YoG",
        "d": "1472x3200",
        "n": str(i),
        "t": "/thumbs/ma_0{}.jpg".format(i),
        "u": "ma_0{}.jpg".format(i)
    }
    odyssey_data.append(entry)

with open("mutedAesthetics.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
