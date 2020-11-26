from collections import defaultdict
neg, pos = defaultdict(int), defaultdict(int)

for _ in range(int(input())):
    f, s = [int(x) for x in input().split()]
    diff = int(f - s)
    if diff > 0:
        pos[diff] += 1 # diffs är positiv om f vinner, negativ om s vinner, 0or sorteras bort (spelar ingen roll)
    elif diff < 0:
        neg[-diff] += 1

positivesgreaterthan, negativeslessthan = [sum(iter(pos.values()))], [sum(iter(neg.values()))]

try:
    posmax = max(iter(pos.keys()))
except:
    posmax = 0
try:
    negmax = max(iter(neg.keys()))
except:
    negmax = 0
largestdiff = max(posmax, negmax)

for val in range(1, largestdiff+1):
    positivesgreaterthan.append(positivesgreaterthan[-1] - pos[val])
    negativeslessthan.append(negativeslessthan[-1] - neg[val])

diffs = [positivesgreaterthan[i] - negativeslessthan[i] for i in range(largestdiff+1)]
print(diffs.index(max(diffs)))

# testing/vis
# from matplotlib import pyplot as plt
# x1 = [5, 6, 7]
# x2 = [6, 8, 2]
# k = [0, 1, 2, 3, 4, 5]
# y = [sum([(x1[i] - x2[i])/(abs(x1[i] - x2[i])) if not abs(x1[i] - x2[i]) <= j else 0 for i in range(len(x1))]) for j in k]
# plt.plot(k, y)
# plt.show()