import json

odyssey_data = []

for i in range(1, 38):
    entry = {

         "a": "Yog",
            "c": "Free",
            "d": "1720x3728",
            "n": f"Holi {i}",
            "t": f"https://one4wall.nyc3.cdn.digitaloceanspaces.com/Walls/FreeWallpapers/Thumbs/holi_00{i}.jpg",
            "u": f"https://one4wall.nyc3.cdn.digitaloceanspaces.com/Walls/FreeWallpapers/holi_00{i}.jpg",
            "g": "Holi"
    }
    odyssey_data.append(entry)

with open("holi.json", "w") as json_file:
    json.dump(odyssey_data, json_file, indent=2)


