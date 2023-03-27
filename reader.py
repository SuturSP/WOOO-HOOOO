import csv
with open('stage3_test.csv', 'r', encoding="utf-8") as f:
    with open('myfile.csv', 'w', encoding="utf-8") as m:
        reader = csv.DictReader(f)
        fieldnames = ["Id", "Images", "Title", "Description", "Price"]
        writer = csv.DictWriter(m, fieldnames = fieldnames)
        writer.writeheader()
        for item in reader:
            tmp = item['Images'].split(',')
            if len(tmp) >= 4:
                writer.writerow(item)