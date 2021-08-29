from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)
n = int(input())
tree = defaultdict(list)
leavesinsubtree = defaultdict(int)
if n == 1:
    print(1)
    exit()

inp = [int(x) for x in input().split()]
for node, parent in enumerate(inp, start=2):
    tree[parent].append(node)

def leavesinsubtreerootedat(node):
    if node not in tree.keys():
        leavesinsubtree[node] = 1
    else:
        for ch in tree[node]:
            leavesinsubtreerootedat(ch)
        leavesinsubtree[node] = sum(leavesinsubtree[a] for a in tree[node])

leavesinsubtreerootedat(1)
print(leavesinsubtree)