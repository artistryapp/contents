data = [
    {
        "a": "YoG",
        "d": "1720x3728",
        "c": "Anime",
        "n": "",
        "t": f"zeel_00{n}.jpg",
        "u": f"zeel_00{n}.jpg"
    }
    for n in range(1557, 1628)
]

import json

# Convert to formatted JSON string
formatted_json = json.dumps(data, indent=2)
print(formatted_json)