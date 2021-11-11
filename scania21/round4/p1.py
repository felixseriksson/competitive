grid = [[None, 2, None, 3, None, 3, None],
        [2, None, 3, None, None, None, 3],
        [None, None, None, 3, 2, None, 4],
        [None, 5, None, 4, None, 4, None],
        [2, None, None, 3, None, None, 3],
        [None, 6, 3, None, None, None, None],
        [None, None, None, 2, 1, 2, 1]]

def ternary(n):
    if n == 0:
        return "0"*27
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    a = ''.join(reversed(nums))
    return (27-len(a))*"0" + a

def fill(n):
    newgrid = [grid[i][:] for i in range(7)]
    t = ternary(n)

    ind = 0
    for i in range(7):
        for j in range(7):
            if newgrid[i][j] == None:
                newgrid[i][j] = t[ind]
                ind += 1
    return newgrid

def check(grid):
    for i in range(7):
        for j in range(7):
            if isinstance(grid[i][j], str):
                cnt = 0
                for oi, oj in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                    try:
                        assert 0 <= i+oi and 0 <= j+oj and i+oi <= 7-1 and j+oj <= 7-1
                        assert isinstance(grid[i+oi][j+oj], int)
                        cnt += grid[i+oi][j+oj]
                    except:
                        pass
                if int(grid[i][j]) != cnt:
                    return False
    return True

print(ternary(3**27))

for i in range(10**12):
    _ = i
    if i % 10**9 == 1:
        print(i)
print("f")