rows, cols = [int(x) for x in input().split()]
startrow = None
endrow = None
for i in range(1, rows + 1):
    r = [char for char in input()]
    if not startrow:
        if "B" in r:
            bcol = (r.index("B") + cols - r[::-1].index("B") - 1)//2 + 1
            startrow = i
            endrow = i
    else:
        if "B" in r:
            endrow = i
brow = (startrow + endrow)//2
print(brow, bcol)