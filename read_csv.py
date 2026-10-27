import csv

with open("data.csv", newline="", encoding="utf-8") as f:
    # 注意看这里，把 reader 换成了 DictReader
    reader = csv.DictReader(f)
    
    for row in reader:
        age = int(row["age"])
        if age > 30:
            print(row["name"], age, row["city"])