inp = """LA-sn
LA-mo
LA-zs
end-RD
sn-mo
end-zs
vx-start
mh-mo
mh-start
zs-JI
JQ-mo
zs-mo
start-JQ
rk-zs
mh-sn
mh-JQ
RD-mo
zs-JQ
vx-sn
RD-sn
vx-mh
JQ-vx
LA-end
JQ-sn"""

# inp = """fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW"""

# inp = """dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc"""

# inp = """start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end"""

from collections import defaultdict, deque
import copy
g = defaultdict(list)

inp = inp.split("\n")
for line in inp:
    a, b = line.split("-")
    g[a].append(b)
    g[b].append(a)

# part 1
# ans = 0
# def dfs(g, v, seen):
#     newseen = copy.deepcopy(seen)
#     newseen[v] = 1
#     for to in g[v]:
#         if to == "start":
#             continue
#         elif to == "end":
#             global ans
#             ans += 1
#         elif to.upper() != to and not newseen[to]:
#             dfs(g, to, newseen)
#         elif to.upper() == to:
#             dfs(g, to, newseen)
#         else:
#             continue

# dfs(g, "start", defaultdict(int))
# print(ans)

# part 1
ans = 0

def dfs(g, v, seen):
    newseen = copy.deepcopy(seen)
    if v.upper() != v:
        newseen[v] += 1
    for to in g[v]:
        if to == "start":
            continue
        elif to == "end":
            global ans
            ans += 1
            continue
        elif to.upper() == to:
            dfs(g, to, newseen)
        elif to.upper() != to:
            if 2 in newseen.values():
                if newseen[to] == 0:
                    dfs(g, to, newseen)
                else:
                    continue
            else:
                if newseen[to] < 2:
                    dfs(g, to, newseen)
                else:
                    continue
dfs(g, "start", defaultdict(int))
print(ans)