from collections import defaultdict
count = defaultdict(int)
count2 = defaultdict(int)
inpp = []

for _ in range(int(input())):
    n = input()
    pn = n.split()[0]
    inpp.append(n)
    count[pn] += 1

for key in count.keys():
    count2[key] = 1

for n in inpp:
    pn = n.split()[0]
    if count[pn] == 1:
        print(n)
    else:
        number = count2[pn]
        count2[pn] += 1
        try:
            pn, rest = n.split(" ", 1)
            print(f"{pn} {number}. {rest}")
        except:
            print(f"{n} {number}.")