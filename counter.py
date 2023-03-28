import json
with open('RomeoAndJuliet.json', 'r', encoding="utf-8") as f:
        data = json.load(f)
        characters = {}
        for act in data["acts"]:
                for scene in act["scenes"]:
                        for item in scene["action"]:
                                name = item["character"]
                                if name not in characters:
                                        characters[name] = 1
                                else:
                                        characters[name] +=1
print(max(characters, key=lambda key: characters[key]))
