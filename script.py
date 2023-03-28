import json
with open('RomeoAndJuliet.json', 'r', encoding="utf-8") as f:
        data = json.load(f)
        characters = {}
        for act in data["acts"]:
                for scene in act["scenes"]:
                        characters[scene["title"]] = []
                        for item in scene["action"]:
                                name = item["character"]
                                if name not in characters[scene["title"]]:
                                        characters[scene["title"]].append(name)
with open('myfile.json', 'w', encoding="utf-8") as l:
        json.dump(characters, l, ensure_ascii=False, indent=4)
