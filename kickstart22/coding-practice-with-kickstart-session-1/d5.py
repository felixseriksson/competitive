from collections import deque, defaultdict

OFFSETS = [(-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1), (0, -1)]

def countcolours(g):
    nb, nr = 0, 0
    for line in g:
        for c in line:
            if c == "B":
                nb += 1
            elif c == "R":
                nr += 1
            else:
                pass
    return nb, nr

def bfs(start, dest, nodes, edges):
    visited = defaultdict(bool)
    prev = defaultdict(bool)
    visited[start] = True
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for other in edges[node]:
            if not visited[other]:
                visited[other] = True
                queue.append(other)
                prev[other] = node
                if other == dest:
                    break
    
    return traceroute(start, dest, prev)


def traceroute(start, dest, prev):
    ret = []
    node = dest
    while node:
        ret.append(node)
        node = prev[node]
    if (-2, -2) in ret:
        ret.remove((-2, -2))
    if (-1, -1) in ret:
        ret.remove((-1, -1))
    return ret[::-1]

for ind in range(int(input())):
    n = int(input())
    grid = [[char for char in input()] for _ in range(n)]

    nblue, nred = countcolours(grid)
    if nblue > nred+1 or nred > nblue + 1:
        print(f"Case #{ind+1}: Impossible")
        continue
    
    bluenodes, blueedges, rednodes, rededges = set(), defaultdict(set), set(), defaultdict(set)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "B":
                bluenodes.add((i, j))
            elif grid[i][j] == "R":
                rednodes.add((i, j))
            else:
                continue
    
    for ci, cj in bluenodes:
        for oi, oj in OFFSETS:
            if (ci + oi, cj + oj) in bluenodes:
                blueedges[(ci, cj)].add((ci + oi, cj + oj))
                blueedges[(ci + oi, cj + oj)].add((ci, cj))
    
    for ci, cj in rednodes:
        for oi, oj in OFFSETS:
            if (ci + oi, cj + oj) in rednodes:
                rededges[(ci, cj)].add((ci + oi, cj + oj))
                rededges[(ci + oi, cj + oj)].add((ci, cj))

    for node in bluenodes:
        if node[1] == 0:
            blueedges[node].add((-1, -1))
            blueedges[(-1, -1)].add(node)
        if node[1] == n-1:
            blueedges[node].add((-2, -2))
            blueedges[(-2, -2)].add(node)
    
    bluenodes.add((-1, -1))
    bluenodes.add((-2, -2))

    for node in rednodes:
        if node[0] == 0:
            rededges[node].add((-1, -1))
            rededges[(-1, -1)].add(node)
        if node[0] == n-1:
            rededges[node].add((-2, -2))
            rededges[(-2, -2)].add(node)

    rednodes.add((-1, -1))
    rednodes.add((-2, -2))

    # OBS: colouredges.values() innehåller EJ alla noder av färg colour
    # Specifikt ej de noder som är isolerade.

    bluepaths = 0
    blueshortestpath = bfs((-1, -1), (-2, -2), bluenodes, blueedges)
    if len(blueshortestpath) > 0:
        bluepaths += 1
        for node in blueshortestpath:
            bluenodes.remove(node)
            for other in blueedges[node]:
                blueedges[other].remove(node)
            blueedges[node] = set()

        blueshortestpath = bfs((-1, -1), (-2, -2), bluenodes, blueedges)
        if len(blueshortestpath) > 0:
            bluepaths += 1

    redpaths = 0
    redshortestpath = bfs((-1, -1), (-2, -2), rednodes, rededges)
    if len(redshortestpath) > 0:
        redpaths += 1
        for node in redshortestpath:
            rednodes.remove(node)
            for other in rededges[node]:
                rededges[other].remove(node)
            rededges[node] = set()

        redshortestpath = bfs((-1, -1), (-2, -2), rednodes, rededges)
        if len(redshortestpath) > 0:
            redpaths += 1

    if bluepaths == 0 and redpaths == 0:
        print(f"Case #{ind+1}: Nobody wins")
    elif bluepaths == 1 and redpaths == 0 and nblue >= nred:
        print(f"Case #{ind+1}: Blue wins")
    elif redpaths == 1 and bluepaths == 0 and nred >= nblue:
        print(f"Case #{ind+1}: Red wins")
    else:
        print(f"Case #{ind+1}: Impossible")