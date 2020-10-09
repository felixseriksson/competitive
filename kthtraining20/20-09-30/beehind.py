def cont(x, y):
    if x == 0 and y == 0:
        exit(0)
    elif x + y == 13:
        print("Never speak again.")
    elif x == y:
        print("Undecided.")
    elif x > y:
        print("To the convention.")
    elif y > x:
        print("Left beehind.")
    else:
        print("this should NEVER happen")
    global a, b
    a, b = [int(x) for x in input().split()]
a, b = [int(x) for x in input().split()]
while True:
    cont(a, b)