import csv
import collections
with open('stage3_test.csv', 'r', encoding="utf-8") as f:
    cnt = collections.Counter()
    b = collections.OrderedDict([])
    reader = csv.reader(f)
    next(reader)
    for item in reader:
        b[item[2]] = float(item[4])
b = collections.OrderedDict(sorted(b.items(), key=lambda t: t[1]))
a = collections.OrderedDict(reversed(b.items()))
print(a, b)
