from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)
n = int(input())
children = defaultdict(list)
coloursneeded = defaultdict(int)
if n == 1:
    print(1)
    exit()

inp = [int(x) for x in input().split()]
for node, parent in enumerate(inp, start = 2):
    children[parent].append(node)

def needed(node):
    if node not in children.keys():
        coloursneeded[node] = 1
        return 1
    val = int(sum([needed(a) for a in children[node]]))
    coloursneeded[node] = val
    return val

needed(1)
print(*sorted(coloursneeded.values()), sep= " ")