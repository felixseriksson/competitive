for case in range(int(input())):
    x, y = [int(x) for x in input().split()]
    # x*b^a = y
    # b^a = y/x
    if y % x == 0:
        print(f"{1} {y//x}")
    else:
        print("0 0")