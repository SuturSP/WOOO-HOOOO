import json
import collections

with open('RomeoAndJuliet.json', 'r', encoding="utf-8") as f:
    a = []
    cnt = collections.Counter()
    data = json.load(f)
    for act in data["acts"]:
        for scene in act["scenes"]:
            for item in scene["action"]:
                text = item["says"][0].lower()
                text = text.replace('.', '')
                text = text.replace(',', '')
                text = text.replace('!', '')
                text = text.replace('?', '')
                text = text.replace(';', '')
                text = text.replace(':', '')
                text = text.split(' ')
                a.extend(text)
                for word in a:
                    cnt[word] += 1
print(cnt.most_common(20))
print(cnt.most_common()[:-20-1:-1] )