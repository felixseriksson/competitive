inp = """target area: x=117..164, y=-140..-89"""
# inp = """target area: x=20..30, y=-10..-5"""

inp = inp.strip().split(" ")[2:]
x = [int(inp[0][2:].split("..")[0]), int(inp[0][2:].split("..")[1][:-1])]
y = [int(inp[1][2:].split("..")[0]), int(inp[1][2:].split("..")[1])]

def calc(bx, by):
    besty = -1*float("inf")
    l = []
    for vx in range(0, bx[1]+1):
        # brute force baby
        for vy in range(3*by[0], -3*by[0]+1):
            vcx, vcy = vx, vy
            cbesty = 0
            xc, yc = 0,0
            while True:
                if bx[0] <= xc <= bx[1] and by[0] <= yc <= by[1]:
                    besty = max(besty, cbesty)
                    l.append([vx, vy])
                    break
                elif xc > bx[1] or yc < by[0]:
                    break
                xc += vcx
                yc += vcy
                vcy -= 1
                vcx -= 1 if vcx > 0 else 0
                cbesty = max(cbesty, yc)
    return besty, l

besty, l = calc(x, y)
# part 1
print(besty)
# part 2
print(len(l))