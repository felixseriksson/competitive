from collections import defaultdict
with open("b/main.txt", "r") as inputfile:
    inp = [line.strip() for line in inputfile]

cases = int(inp[0])
i = 1
out = []

for case in range(1, cases + 1):
    n, m, a, b = [int(x) for x in inp[i].split(" ")]
    i += 1
    
    if n + m - 1 > a or n + m - 1 > b:
        print(f"Case #{case}: Impossible")
        out.append(f"Case #{case}: Impossible")
    else:
        print(f"Case #{case}: Possible")
        out.append(f"Case #{case}: Possible")
        topleft = a - n - m + 2
        bottomleft = b - n - m + 2
        grid = [[1]*m for _ in range(n)]
        grid[0][0] = topleft
        grid[-1][0] = bottomleft
        for row in grid:
            print(" ".join([str(k) for k in row]))
            out.append(" ".join([str(k) for k in row]))

with open("b/main-out.txt", "w") as outfile:
    for line in out:
        outfile.write(line + "\n")