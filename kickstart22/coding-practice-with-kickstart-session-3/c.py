for case in range(1, int(input())+ 1):
    n, r, c, sr, sc = [int(x) for x in input().split()]
    cr, cc = sr, sc
    instruction = input()
    above, below, rightof, leftof = dict(), dict(), dict(), dict()
    affected = set()
    # for i in range(1, r + 1):
    #     for j in range(1, c + 1):
    #         above[(i, j)] = (i - 1, j)
    #         below[(i, j)] = (i + 1, j)
    #         rightof[(i, j)] = (i, j + 1)
    #         leftof[(i, j)] = (i, j - 1)
    for char in instruction:
        try:
            abovecr, abovecc = above[(cr, cc)]
        except:
            abovecr, abovecc = (cr - 1, cc)
        try:
            belowcr, belowcc = below[(cr, cc)]
        except:
            belowcr, belowcc = (cr + 1, cc)
        try:
            rightofcr, rightofcc = rightof[(cr, cc)]
        except:
            rightofcr, rightofcc = (cr, cc + 1)
        try:
            leftofcr, leftofcc = leftof[(cr, cc)]
        except:
            leftofcr, leftofcc = (cr, cc - 1)
        below[(abovecr, abovecc)] = (belowcr, belowcc)
        above[(belowcr, belowcc)] = (abovecr, abovecc)
        leftof[(rightofcr, rightofcc)] = (leftofcr, leftofcc)
        rightof[(leftofcr, leftofcc)] = (rightofcr, rightofcc)
        if char == "N":
            try:
                cr, cc = above[(cr, cc)]
            except:
                cr, cc = (cr - 1, cc)
        elif char == "S":
            try:
                cr, cc = below[(cr, cc)]
            except:
                cr, cc = (cr + 1, cc)
        elif char == "E":
            try:
                cr, cc = rightof[(cr, cc)]
            except:
                cr, cc = (cr, cc + 1)
        elif char == "W":
            try:
                cr, cc = leftof[(cr, cc)]
            except:
                cr, cc = (cr, cc - 1)
        else:
            print("Error")
            exit("This should not happen")

    print(f"Case #{case}: {cr} {cc}")