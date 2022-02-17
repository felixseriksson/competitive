from collections import deque

def findcomponents(grid, char):
    offsets = [(0, -1), (-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1)]
    ret = []
    seen = set()
    for i in range(1, len(grid)):
        for j in range(1, len(grid)):
            if (i, j) in seen or grid[i][j] != char:
                continue
            else:
                comp = [(i, j)]
                seen.add((i, j))
                q = deque([(i, j)])
                while len(q) > 0:
                    ci, cj = q.popleft()
                    for oi, oj in offsets:
                        if (ci + oi, cj + oj) in seen or grid[ci+oi][cj+oj] != char:
                            continue
                        else:
                            seen.add((ci + oi, cj + oj))
                            q.append((ci + oi, cj + oj))
                            comp.append((ci + oi, cj + oj))
                ret.append(comp)
    return ret

def getverdict(grid):
    bluecomponents = findcomponents(grid, "B")
    redcomponents = findcomponents(grid, "R")
    bluehaspath, redhaspath = False, False
    for comp in bluecomponents:
        onleft = [c for c in comp if c[1] == 1]
        onright = [c for c in comp if c[1] == len(grid)-2]
        if len(onleft) > 0 and len(onright) > 0:
            bluehaspath = True
    for comp in redcomponents:
        ontop = [c for c in comp if c[0] == 1]
        onbottom = [c for c in comp if c[0] == len(grid)-2]
        if len(ontop) > 0 and len(onbottom) > 0:
            redhaspath = True
    if bluehaspath and redhaspath:
        return "Impossible"
    elif bluehaspath and not redhaspath:
        return "Blue wins"
    elif not bluehaspath and redhaspath:
        return "Red wins"
    else:
        return "Nobody wins"

for ind in range(int(input())):
    n = int(input())
    g = [["#" for _ in range(n+2)]]
    for _ in range(n):
        l = ["#"]
        l.extend([char for char in input()])
        l.append("#")
        g.append(l)
    g.append(["#" for _ in range(n+2)])

    nred, nblue = 0, 0
    for line in g:
        for char in line:
            if char == "R":
                nred += 1
            elif char == "B":
                nblue += 1
    if abs(nred-nblue) > 1:
        print(f"Case #{ind+1}: Impossible")
        continue
    else:
        bluelegitwins, redlegitwins, impossible = False, False, False
        for i in range(1, n+2):
            for j in range(1, n+2):
                if g[i][j] == "B":
                    g[i][j] = "."
                    oldverdict = getverdict(g)
                    g[i][j] = "B"
                    newverdict = getverdict(g)
                    if oldverdict == "Nobody wins" and newverdict == "Blue wins":
                        bluelegitwins = True
                    elif newverdict == "Impossible":
                        impossible = True
                    else:
                        pass
                elif g[i][j] == "R":
                    g[i][j] = "."
                    oldverdict = getverdict(g)
                    g[i][j] = "R"
                    newverdict = getverdict(g)
                    if oldverdict == "Nobody wins" and newverdict == "Red wins":
                        redlegitwins = True
                    elif newverdict == "Impossible":
                        impossible = True
                    else:
                        pass
        if bluelegitwins and redlegitwins:
            impossible = True
            print("both bluelegitwins and redlegitwins should not be true!")
        if impossible:
            print(f"Case #{ind+1}: Impossible")
        else:
            if bluelegitwins:
                print(f"Case #{ind+1}: Blue wins")
            elif redlegitwins:
                print(f"Case #{ind+1}: Red wins")
            else:
                print(f"Case #{ind+1}: Nobody wins")