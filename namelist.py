import json
import collections

with open('RomeoAndJuliet.json', 'r', encoding="utf-8") as f:
    a = []
    data = json.load(f)
    d = collections.defaultdict(list)
    cnt = collections.Counter()
    for act in data["acts"]:
        for scene in act["scenes"]:
            for item in scene["action"]:
                k = item["character"]
                v = item["says"]
                d[k].extend(v)
                for k in d:
                    for v in d[k]:
                        a.append(k)
for elem in a:
    cnt[elem] += 1
print(cnt.most_common())