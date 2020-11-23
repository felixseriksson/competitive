from collections import defaultdict
längd = int(input())
antalvokaler = int(input())
word = input()
VOKALER = set(["A", "E", "I", "O", "U", "Y"])
pos = []
for i in range(längd):
    if word[i] in VOKALER:
        pos.append(i)
indexes = zip(pos, pos[antalvokaler-1:])
di = defaultdict(set)
lastindex = 0
for left, right in indexes:
    suffix = word[left:right+1]
    prefix = word[lastindex:left]
    for s in [prefix[-i:] for i in range(1, len(prefix) + 1)]:
        di[suffix].add(s)
    lastindex = left+1

print(max([len(k) for k in di.values()]) + 1)