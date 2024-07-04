import json

odyssey_data = []

for i in range(1, 57):
    entry = {
       "a": "YoG",
        "d": "1720x3728",
        "n": str(i),
        "t": "/thumbs/StockAlike_{}.jpg".format(i),
        "u": "StockAlike_{}.jpg".format(i)
    }
    odyssey_data.append(entry)

with open("alike.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)
