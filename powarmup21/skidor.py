r, c, l = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(r)]
globalmin = min(min(row[:l]) for row in grid[:l])
globalmax = max(max(row[:l] for row in grid:l))
globalrow = 0
globalcol = 0
grid = [0 for ]

# for frow in range(r-l+1):
#     for fcol in range(c-l+1):
#         mini = min([min(line[fcol: fcol + l]) for line in grid[frow: frow + l]])
#         if mini == -1:
#             diff[frow][fcol] = float("inf")
#         else:
#             df = max([max(line[fcol: fcol + l]) for line in grid[frow: frow + l]]) - mini
#             diff[frow][fcol] = df
#             if df < globalmindiff:
#                 globalmindiff = df
#                 globalmindiffrow = frow
#                 globalmindiffcol = fcol
# print(globalmindiffrow, globalmindiffcol)
rowmin = globalmindiff
rowrow = globalmindiffrow
rowcol = globalmindiffcol

for rowleft in range(c - l + 1):
    for colleft in range(r - l):
        scanmin = min([k[l + colleft] for k in grid[rowleft:rowleft+l]])
    newrowscanmin = min(grid[l + rowleft][:l])
    if newrowscanmin < rowmin:
        rowmin = newrowscanmin
        rowrow = rowleft
        rowcol = 0