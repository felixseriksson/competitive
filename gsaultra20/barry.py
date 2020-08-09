def dist(x1, x2):
    return abs(x1-x2)

def solution(a, b):
    a.insert(0, 0)
    b.insert(0, 0)
    grid = [[0 for i in range(len(b))] for j in range(len(a))]
    place = [[0 for i in range(len(b))] for j in range(len(a))]
    d = 0
    for i in range(1, len(a)):
        d += dist(a[i-1], a[i])
        grid[i][0] = d
        place[i][0] = a[i]
    d = 0
    for i in range(1, len(b)):
        d += dist(b[i-1], b[i])
        grid[0][i] = d
        place[0][i] = b[i]
    #print(place)
    #print(grid)
    for it in range(1, len(a)):
        for jt in range(1, len(b)):
            upperval = grid[it-1][jt]
            upperplace = place[it-1][jt]
            leftval = grid[it][jt-1]
            leftplace = place[it][jt-1]
            if upperval + dist(upperplace, a[it]) <= leftval + dist(leftplace, b[jt]):
                grid[it][jt] = upperval + dist(upperplace, a[it])
                place[it][jt] = a[it]
            else:
                grid[it][jt] = leftval + dist(leftplace, b[jt])
                place[it][jt] = b[jt]
            #grid[it][jt] = min(grid[it-1][jt], grid[it][jt-1]) + dist(a[it], b[jt]) #min([grid[it-1][index] + dist(a[it], b[index]) for index in range(jt, len(b))])

    return grid[-1][-1]

print(solution([5, 3, 10, 6], [9, 7, 12]))