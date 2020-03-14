import csv

f = r'journal_access.csv'

d = {}
asd = []
#trolig tre läkare som betett sig kontigt - matcha dem.
#['doctor_id', 'timestamp', 'patient_zip']
l = []
with open(f) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    i = 0
    for row in csv_reader:
        if i == 0:
            i += 1
            continue
        k = row
        if "SSM" in k[0]:
            l.append(k)


l = sorted(l,key=lambda x: x[0][4])

for el in l:
    if el[0] in d:
        d[el[0]] +=1
    else:
        d[el[0]] = 1

maxx = 0
s = ""
for key in d.keys():
    if d[key] > maxx:
        maxx = d[key]
        s = key

print(s)
print(d["SSM{unu6"])