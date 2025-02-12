data = [
    {
        "a": "YoG",
        "d": "1472x3200",
        "n": str(n),
        "t": "/thumbs/cosmic_00{}.jpg".format(n),
        "u": "cosmic_00{}.jpg".format(n)
    }
    for n in range(1, 30)
]

import json

# Convert to formatted JSON string
formatted_json = json.dumps(data, indent=2)

print(formatted_json)