import json
import collections

with open('RomeoAndJuliet.json', 'r', encoding="utf-8") as f:
    data = json.load(f)
    d = collections.defaultdict(list)
    for act in data["acts"]:
        for scene in act["scenes"]:
            for item in scene["action"]:
                k = item["character"]
                v = item["says"]
                d[k].append(v)
print(d)
