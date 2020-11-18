r, c, l = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(r)]
mingrid = [[0 for _ in range(c - l + 1)] for _ in range(r - l + 1)]
maxgrid = [[0 for _ in range(c - l + 1)] for _ in range(r - l + 1)]

for rowind in range(r- l + 1):
    # computea första rutan
    minofsquare = min([min(row[:l]) for row in grid[rowind: rowind + l]])
    maxofsquare = max([max(row[:l]) for row in grid[rowind: rowind + l]])
    mingrid[rowind][0] = minofsquare
    maxgrid[rowind][0] = maxofsquare
    for colind in range(c - l):
        newcolmin = min(row[l+colind] for row in grid[rowind: rowind + l])
        newcolmax = max(row[l+colind] for row in grid[rowind: rowind + l])
        oldcolmin = min(row[colind] for row in grid[rowind: rowind + l])
        oldcolmax = max(row[colind] for row in grid[rowind: rowind + l])
        if maxgrid[rowind][colind] != oldcolmax:
            maxgrid[rowind][colind+1] = max(maxgrid[rowind][colind], newcolmax)
        else:
            maxgrid[rowind][colind+1] = max([max(row[colind + 1:colind + l + 1]) for row in grid[rowind: rowind + l]])
        if mingrid[rowind][colind] != oldcolmin:
            mingrid[rowind][colind+1] = min(mingrid[rowind][colind], newcolmin)
        else:
            mingrid[rowind][colind+1] = min([min(row[colind + 1:colind + l + 1]) for row in grid[rowind: rowind + l]])
# for row in maxgrid:
#     print(row)
# for row in mingrid:
#     print(row)

# print(max([max([max(abs(mingrid[rowind][colind] - maxgrid[rowind][colind])) if mingrid[rowind][colind] != -1 else -1 for colind in range(r - l + 1)]) for rowind in range(r - l + 1)]))
glmaxdiff = float("inf")
glmaxrow = 0
glmaxcol = 0
for row in range(r-l+1):
    for col in range(c-l+1):
        if not mingrid[row][col] == -1:
            if abs(maxgrid[row][col] - mingrid[row][col]) < glmaxdiff:
                glmaxdiff = abs(maxgrid[row][col] - mingrid[row][col])
                glmaxrow = row
                glmaxcol = col

print(glmaxrow, glmaxcol)