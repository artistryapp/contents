import json

odyssey_data = []

for i in range(56, 114):
    entry = {
       "a": "YoG",
        "d": "1720x3728",
        "n": str(i),
        "t": "/thumbs/Kawaii_Cutesy_{}.jpg".format(i),
        "u": "Kawaii_Cutesy_{}.jpg".format(i)
    }
    odyssey_data.append(entry)

with open("KawaiiCutesy.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
