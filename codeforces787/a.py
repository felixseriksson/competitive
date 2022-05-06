for case in range(int(input())):
    a, b, c, x, y = [int(x) for x in input().split()]
    x = max(0, x-a)
    y = max(0, y-b)
    if c >= x + y:
        print("YES")
    else:
        print("NO")