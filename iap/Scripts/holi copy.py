import json

odyssey_data = []

for i in range(1, 35):
    entry = {

         "a": "Yog",
            "c": "Free",
            "d": "1720x3728",
            "n": f"Easter {i}",
            "t": f"https://one4wall.nyc3.cdn.digitaloceanspaces.com/Walls/FreeWallpapers/Thumbs/easter_00{i}.jpg",
            "u": f"https://one4wall.nyc3.cdn.digitaloceanspaces.com/Walls/FreeWallpapers/easter_00{i}.jpg",
            "g": "Easter"
    }
    odyssey_data.append(entry)

with open("easter.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)


