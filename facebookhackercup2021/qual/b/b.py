with open("b/main.txt", "r") as inputfile:
    inp = [line.strip() for line in inputfile]

cases = int(inp[0])
i = 1
out = []

for ind in range(1,cases+1):
    n = int(inp[i])
    i += 1
    board = []
    for _ in range(n):
        board.append(inp[i])
        i += 1
    minreq, occurrences = 10000000, 0
    seen = set()
    
    for x, row in enumerate(board):
        if "O" not in row:
            req = sum([1 if char == "." else 0 for char in row])
            if req == 1:
                y = row.index(".")
                if (x,y) in seen:
                    pass
                else:
                    if req < minreq:
                        minreq = req
                        occurrences = 1
                        seen.add((x,y))
                    elif req == minreq:
                        occurrences += 1
                        seen.add((x,y))
            else:
                if req < minreq:
                    minreq = req
                    occurrences = 1
                elif req == minreq:
                    occurrences += 1
    board = [list(z) for z in zip(*board)]
    for x, row in enumerate(board):
        if "O" not in row:
            req = sum([1 if char == "." else 0 for char in row])
            if req == 1:
                y = row.index(".")
                if (y,x) in seen:
                    pass
                else:
                    if req < minreq:
                        minreq = req
                        occurrences = 1
                    elif req == minreq:
                        occurrences += 1
            else:
                if req < minreq:
                    minreq = req
                    occurrences = 1
                elif req == minreq:
                    occurrences += 1

    if occurrences == 0:
        out.append(f"Case #{ind}: Impossible")
    else:
        out.append(f"Case #{ind}: {minreq} {occurrences}")


with open("b/main-out.txt", "w") as outfile:
    for line in out:
        outfile.write(line + "\n")