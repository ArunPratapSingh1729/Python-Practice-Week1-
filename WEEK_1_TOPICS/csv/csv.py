import csv

#read
with open('file.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row)

#DictRead
with open('file.csv') as f:
    reader = csv.DictReader(f)
    # next(reader)  never add this when read in dic format
    for row in reader:
        print(row)

#skip header
with open('file.csv') as f:
    reader = csv.DictReader(f)
    next(reader)
    for row in reader:
        print(row)  


#write
with open('file.csv','w',newline="") as f:
    writer = csv.DictWriter(f , fieldnames = ['name', 'age'])
    writer.writeheader()
    writer.writerows([{"name":"arun","age":12}])

#DictWrite
with open('file.csv','w',newline="") as f:
    writer = csv.DictWriter(f , fieldnames = ['name', 'age'])
    writer.writeheader()
    writer.writerows([{"name":"arun","age":12}])