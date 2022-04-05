for case in range(1, int(input()) + 1):
    print(f"Case #{case}:")
    r, c = [int(x) for x in input().split()]
    for i in range(2*r+1):
        if i == 0:
            print(".." + "+-"*(c-1) + "+")
        elif i == 1:
            print(".." + "|."*(c-1) + "|")
        elif i % 2 == 0:
            print("+-"*c + "+")
        else:
            print("|."*c + "|")