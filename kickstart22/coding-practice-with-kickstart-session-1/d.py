from collections import deque

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

def findcomponents(g):
    offsets = [(0, -1), (-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1)]
    ret = []
    seen = set()
    for i in range(1, len(grid)):
        for j in range(1, len(grid)):
            if (i, j) in seen or g[i][j] == "." or g[i][j] == "#":
                continue
            else:
                comp = [(i, j)]
                seen.add((i, j))
                q = deque([(i, j)])
                char = grid[i][j]
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

def potentialwinningpaths(cs, g):
    ret = []
    n = len(g) - 2
    for c in cs:
        clr = g[c[0][0]][c[0][1]]
        if clr == "B":
            lc = [c[i] for i in range(len(c)) if c[i][1] == 1]
            rc = [c[i] for i in range(len(c)) if c[i][1] == n]
        elif clr == "R":
            lc = [c[i] for i in range(len(c)) if c[i][0] == 1]
            rc = [c[i] for i in range(len(c)) if c[i][0] == n]
        else:
            print("This should not happen!")
            exit(0)

        if len(lc) > 0 and len(rc) > 0:
            ret.append(c)
    
    return ret

def isoneconnected(c, clr, n):
    ioc = False
    if clr == "B":
        lc = [c[i] for i in range(len(c)) if c[i][1] == 1]
        rc = [c[i] for i in range(len(c)) if c[i][1] == n]
    elif clr == "R":
        lc = [c[i] for i in range(len(c)) if c[i][0] == 1]
        rc = [c[i] for i in range(len(c)) if c[i][0] == n]
    if len(lc) == 1 or len(rc) == 1:
        return True

    for node in c:
        newc = c[:]
        newc.remove(node)
        if isconnected(newc):
            continue
        else:
            ioc = True
    
    return ioc

def isconnected(c):
    if len(c) == 0:
        return False
    offsets = [(0, -1), (-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1)]
    seen = set()
    seen.add(c[0])
    q = deque([c[0]])
    c = set(c)
    while len(q) > 0:
        ci, cj = q.popleft()
        for oi, oj in offsets:
            if (ci + oi, cj + oj) in seen or (ci + oi, cj + oj) not in c:
                continue
            else:
                seen.add((ci + oi, cj + oj))
                q.append((ci + oi, cj + oj))

    if len(c.symmetric_difference(seen)) == 0:
        return True
    else:
        return False


for ind in range(int(input())):
    n = int(input())
    grid = [["#" for _ in range(n+2)]]
    for _ in range(n):
        l = ["#"]
        l.extend([char for char in input()])
        l.append("#")
        grid.append(l)
    grid.append(["#" for _ in range(n+2)])

    # parity check: Om skillnaden i antal lagda är > 1: omöjligt
    # Annars: Hitta alla sammanhängande komponenter
    # Hitta alla som är blå och spänner höger vänster eller röda och spänner upp ner
    # Om det finns noll sådana: ej färdigt.
    # Om det finns totalt 2 eller fler sådana: omöjligt
    # Annars finns exakt en sådan
    # Har den färgen fler än eller lika många lagda som motsatt färg? Om nej, omöjligt, annars...
    # Verifiera att denna är 1-connected: Om ja har den färgen vunnit, annars omöjligt

    nblue, nred = countcolours(grid)
    if nblue > nred+1 or nred > nblue + 1:
        print(f"Case #{ind+1}: Impossible")
    else:
        components = findcomponents(grid)
        components = potentialwinningpaths(components, grid)
        if len(components) == 0:
            print(f"Case #{ind+1}: Nobody wins")
        elif len(components) >= 2:
            print(f"Case #{ind+1}: Impossible")
        else:
            component = components[0]
            colour = grid[component[0][0]][component[0][1]]
            if (colour == "R" and nred < nblue) or (colour == "B" and nblue < nred):
                print(f"Case #{ind+1}: Impossible")
            else:
                if isoneconnected(component, colour, len(grid)-2):
                    colour = "Red" if colour == "R" else "Blue"
                    print(f"Case #{ind+1}: {colour} wins")
                else:
                    print(f"Case #{ind+1}: Impossible")