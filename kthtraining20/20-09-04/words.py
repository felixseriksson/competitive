A, B = input().split()

broke = False
for chara in A:
    for charb in B:
        if chara == charb:
            horizontalindex = A.index(chara)
            verticalindex = B.index(charb)
            broke = True
            break
    if broke is True:
        break
        
for row in range(len(B)):
    if row == verticalindex:
        print(A)
    else:
        rowtoprint = "."*(horizontalindex) + B[row] + "."*((len(A))-horizontalindex-1)
        print(rowtoprint)