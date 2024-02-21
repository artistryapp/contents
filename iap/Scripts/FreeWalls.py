import json

odyssey_data = []

for i in range(303, 274, -1):
    entry = {
      "a": "YoG",
      "d": "1720 x 3728",
      "c": "",
      "n": str(i),
      "t": "zeel_00{}.jpg".format(i),
      "u": "zeel_00{}.jpg".format(i)
    }
    odyssey_data.append(entry)

with open("FreeWalls.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
