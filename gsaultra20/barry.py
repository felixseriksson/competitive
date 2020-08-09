def dist(x1, x2):
    return abs(x1-x2)

def solution(a, b):
    a.insert(0, 0)
    b.insert(0, 0)
    grid = [[0 for i in range(len(b))] for j in range(len(a))]
    d = 0
    for i in range(1, len(a)):
        d += dist(a[i-1], a[i])
        grid[i][0] = d
    d = 0
    for i in range(1, len(b)):
        d += dist(b[i-1], b[i])
        grid[0][i] = d
    for it in range(1, len(a)):
        for jt in range(1, len(b)):
            grid[it][jt] = min(grid[it-1][jt], grid[it][jt-1]) + dist(a[it], b[jt])

    return grid[len(a)-1][len(b)-1]

print(solution([5, 3, 10, 6], [9, 7, 12]))