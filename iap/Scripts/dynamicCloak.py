import json

odyssey_data = []

for i in range(1, 31):
    entry = {
       "a": "YoG",
        "d": "1720x3728",
        "n": str(i),
        "t": "/thumbs/dynamiccloak_0{}.jpg".format(i),
        "u": "dynamiccloak_0{}.jpg".format(i)
    }
    odyssey_data.append(entry)

with open("dynamiccloak.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
