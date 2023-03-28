import json
newdata = dict()
with open('wikidata_1000.json', 'r', encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        x = data["label"]
        y = x["value"]
        if "description" not in data:
            m = "None."
        else:
            z = data['description']
            m = z["value"]
        newdata[y] = m
with open('myfile.json', 'w', encoding="utf-8") as l:
    json.dump(newdata, l, ensure_ascii=False, indent=4)
