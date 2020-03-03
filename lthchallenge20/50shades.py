import re

times = int(input())

counter = 0

for n in range(times):
    string = input()
    x = re.search("rose",string, re.IGNORECASE)
    y = re.search("pink",string, re.IGNORECASE)
    if not(x == None and y == None):
        counter += 1

if counter:
    print(counter)
else:
    print("I must watch Star Wars with my daughter")