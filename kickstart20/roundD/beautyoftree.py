## Tror denna funkar om man bortser från kollisioner (alltså att A kan måla samma som B)
## Det är väl iofs det som är den svåra delen att lösa, antar jag.
## Jag kommer ej på nåt bra...

from collections import deque
from math import ceil

'''
def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm
'''

cases = int(input())
for case in range(1, cases+1):
    N, A, B = [int(x) for x in input().split()]
    tree = {}
    for n in range(1, N+1):
        tree[n] = []
    verts = deque([int(x) for x in input().split()])
    for n in range(2, N+1):
        tree[verts.popleft()].append(n)
    #tree är på formen nod:[barn1, barn2, ...]
    levels = []
    visited = set()
    queue = deque([1, None])
    levelcounter = 0
    while queue:
        curr = queue.popleft()
        if curr == None:
            levels.append(levelcounter)
            levelcounter = 0
            continue
        levelcounter += 1
        if curr not in visited:
            visited.add(curr)
            for nb in tree[curr]:
                queue.append(nb)
            if len(tree[curr]) != 0:
                queue.append(None)
    print(tree)
    print(levels)
    # om a målar var a:te och völjer en nod på djup d så målas ceil(d/a) noder
    val = 0
    levelnum = len(levels)
    for i in range(levelnum):
        for j in range(levelnum):
            val += (ceil((i+1)/A)+ceil((j+1)/B))*(levels[i]/N)*(levels[j]/N)
    print("Case #{}: {}".format(case, val))