numberofboxes = int(input())
boxes = []
for _ in range(numberofboxes):
    ln = input().split()
    boxes.append((int(ln[0]), ln[1]))

rules = []

for rule in ["RGB", "RBG", "BGR", "BRG", "GRB", "GBR"]:
    s = sorted([k for k in boxes if k[1] == rule[0]], key = lambda x: x[0])
    m = sorted([k for k in boxes if k[1] == rule[1]], key = lambda x: x[0])
    l = sorted([k for k in boxes if k[1] == rule[2]], key = lambda x: x[0])
    saved = 0
    ind = 0
    for med in m:
        try: 
            sma = s[ind]
        except IndexError:
            break
        if med[0] > sma[0]:
            ind += 1
    saved += ind
    ind = 0
    for lrg in l:
        try: 
            med = m[ind]
        except IndexError:
            break
        if lrg[0] > med[0]:
            ind += 1
    saved += ind
    rules.append((rule, numberofboxes - saved))

rules = sorted(rules, key = lambda x: x[1])
print(rules[0][0][::-1])
print(rules[0][1])