data = [
    {
        "a": "YoG",
        "d": "1720x3728",
        "c": "Anime",
        "n": "",
        "t": f"ZeelPlus_00{n}.jpg",
        "u": f"ZeelPlus_00{n}.jpg"
    }
    for n in range(1540, 1600)
]

import json

# Convert to formatted JSON string
formatted_json = json.dumps(data, indent=2)

print(formatted_json)