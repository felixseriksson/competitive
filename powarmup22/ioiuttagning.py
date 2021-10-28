n = int(input())
res = [None for _ in range(n)]
for i in range(n):
    res[i] = input().split()
    for j in range(1, 6):
        res[i][j] = int(res[i][j])

for t in range(2, 6):
    scores = [a[t] for a in res]
    maxx = max(scores)
    q, r = divmod(n, 2)
    med = sorted(scores)[q] if r else sum(sorted(scores)[q-1:q+1])/2
    for i in range(n):
        if scores[i] <= med:
            scores[i] *= 50/med
        else:
            scores[i] = 50 + 50*(scores[i]-med)/(maxx-med)
    for i in range(n):
        res[i][t] = scores[i]

finalscores = []
for c in res:
    finalscores.append(c[:3])
    finalscores[-1][-1] += (sum(c[3:]) - min(c[3:]))
finalscores = sorted(finalscores, key = lambda x: x[2], reverse=True)
ioi = sorted(finalscores[:4], key= lambda x: x[0])
finalscores = sorted([a for a in finalscores if a not in ioi and a[1] != 3], key = lambda x: x[2], reverse=True)
boi = sorted(finalscores[:2], key= lambda x: x[0])
print(" ".join([a[0] for a in ioi]))
print(" ".join([a[0] for a in boi]))