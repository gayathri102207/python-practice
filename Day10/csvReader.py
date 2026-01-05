import csv
with open("Day10/StudentData.csv",'r') as data:
    reader=csv.reader(data)
    for row in reader:
        print(*row)