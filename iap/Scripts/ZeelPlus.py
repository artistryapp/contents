import json

odyssey_data = []

for i in range(90, 52, -1):
    entry = {
       "a": "YoG",
        "d": "1472x3200",
        "c": "",
        "n": str(i),
        "t": "ZeelPlus_00{}.jpg".format(i),
        "u": "ZeelPlus_00{}.jpg".format(i)
    }
    odyssey_data.append(entry)

with open("zeelplus.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
