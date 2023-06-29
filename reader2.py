import csv
with open('stage3_test.csv', 'r', encoding="utf-8") as f:
    with open('myfile.csv', 'w', encoding="utf-8") as m:
        reader = csv.reader(f)
        writer = csv.writer(m)
        writer.writerow(["Id", "Images", "Title", "Description", "Price"])
        for item in reader:
            if item[4] != "Price":
                if 10000 < float(item[4]) <= 50000:
                    writer.writerow(item)
