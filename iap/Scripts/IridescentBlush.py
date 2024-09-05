import json

odyssey_data = []

for i in range(1, 107):
    entry = {
       "a": "YoG",
        "d": "1720x3728",
        "n": str(i),
        "t": "/thumbs/is_0{}.jpg".format(i),
        "u": "is_0{}.jpg".format(i)
    }
    odyssey_data.append(entry)

with open("IridescentBlush.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
