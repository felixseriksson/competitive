from collections import defaultdict
testcases = int(input())

for testcase in range(1, testcases+1):
    n = int(input())
    rowmap = defaultdict(set)
    colmap = defaultdict(set)
    trace = 0
    for i in range(n):
        row = [int(x) for x in input().split()]
        for j in range(n):
            item = row.pop(0)
            if i == j:
                trace += item
            rowmap[i].add(item)
            colmap[j].add(item)
    rows = 0
    for row in list(rowmap.values()):
        if len(row) != n:
            rows += 1
    cols = 0
    for col in list(colmap.values()):
        if len(col) != n:
            cols += 1
    print("Case #{}: {} {} {}".format(testcase, trace, rows, cols))