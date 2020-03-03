from collections import Counter
import operator
antalpunkter = int(input())
före = []
efter = []
for n in range(antalpunkter):
    före.append([int(x) for x in input().split()])
for n in range(antalpunkter):
    efter.append([int(x) for x in input().split()])

vektorer = []
for punkti in före:
    for punktj in efter:
        vektorer.append((punkti[0]-punktj[0], punkti[1]-punktj[1]))

förekomster = dict(Counter(vektorer))
print(antalpunkter-max(förekomster.values()))