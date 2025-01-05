import json

odyssey_data = []

for i in range(85, 133):
    entry = {
       "a": "YoG",
        "d": "5824x3264",
        "n": str(i),
        "t": "/thumbs/ZeelDesk_{}.jpg".format(i),
        "u": "ZeelDesk_{}.jpg".format(i)
    }
    odyssey_data.append(entry)

with open("ZeelDeskV1.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
