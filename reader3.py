import csv
with open('stage3_test.csv', 'r', encoding="utf-8") as f:
    with open('myfile.csv', 'w', encoding="utf-8") as m:
        reader = csv.reader(f)
        writer = csv.writer(m)
        for item in reader:
            writer.writerow([item[0],item[2],item[4]])