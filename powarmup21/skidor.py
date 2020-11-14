r, c, l = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(r)]
diff = [[0 for _ in range(c-l+1)] for _ in range(r-l+1)]
globalmindiff = float("inf")
globalmindiffrow = None
globalmindiffcol = None
for frow in range(r-l+1):
    for fcol in range(c-l+1):
        mini = min([min(line[fcol: fcol + l]) for line in grid[frow: frow + l]])
        if mini == -1:
            diff[frow][fcol] = float("inf")
        else:
            df = max([max(line[fcol: fcol + l]) for line in grid[frow: frow + l]]) - mini
            diff[frow][fcol] = df
            if df < globalmindiff:
                globalmindiff = df
                globalmindiffrow = frow
                globalmindiffcol = fcol
print(globalmindiffrow, globalmindiffcol)