from collections import defaultdict
children = defaultdict(list)
for i in range(2, int(input())+1):
    children[int(input())].append(i)

global isspruce
isspruce = True
def issspruce(node):
    lch, nonlch = [], []
    for child in children[node]:
        try:
            a = children[child][0]
            nonlch.append(child)
        except:
            lch.append(child)
    if len(lch) < 3:
        global isspruce
        isspruce = False
        return
    for child in nonlch:
        issspruce(child)

issspruce(1)

if isspruce:
    print("Yes")
else:
    print("No")