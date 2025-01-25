data = [
    {
        "a": "YoG",
        "d": "1720x3728",
        "c": "Anime",
        "n": "",
        "t": f"ZeelPlus_00{n}.jpg",
        "u": f"ZeelPlus_00{n}.jpg"
    }
    for n in range(1275, 1304)
]

import json

# Convert to formatted JSON string
formatted_json = json.dumps(data, indent=2)


with open("plus.json", "w") as json_file:
    json.dump(data, formatted_json, indent=2)

