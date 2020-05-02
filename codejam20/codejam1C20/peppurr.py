testcases = int(input())

def taxidist(x1, y1, x2, y2):
    return abs(x2-x1)+abs(y2-y1)

for testcase in range(1, testcases+1):
    inputs = input().split()
    x, y  = int(inputs[0]), int(inputs[1])
    path = inputs[2]
    counter = 0
    dist = abs(x) + abs(y)
    myx, myy = 0, 0
    found = False
    for step in path:
        counter += 1
        if dist <= 0:
            break
        if step == "S":
            y -= 1
        elif step == "W":
            x -= 1
        elif step == "N":
            y += 1
        elif step == "E":
            x += 1
        dist = abs(x) + abs(y)
        if dist <= counter:
            found = True
            break
    final = counter if found else "IMPOSSIBLE"
        # if step == "S":
        #     y -= 1
        # elif step == "N":
        #     y += 1
        # elif step == "W":
        #     x -= 1
        # elif step == "E":
        #     x += 1
        # #tests = [(myx, myy-1), (myx, myy), (), ()]
        # if y != myy:
        #     if y > myy:
        #         counter += 1
        #         myy += 1
        #     else:
        #         counter += 1
        #         myy -= 1
        # elif x != myx:
        #     if x > myx:
        #         counter += 1
        #         myx += 1
        #     else:
        #         counter += 1
        #         myx -= 1
        # else:
        #     break

    print("Case #{}: {}".format(testcase, final))