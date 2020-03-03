antalstalagmtiter, antalbrev, height, width = [int(x) for x in input().split()]
stalagmtiter = {}
xvärdenförstalagmtiter = []
for n in range(antalstalagmtiter):
    temp = [int(x) for x in input().split()]
    stalagmtiter[temp[1]] = (temp[0], temp[2]) #stalagmtiter[x-värde] = (1=stalagmit eller 2=stalagtit, y-värde)
    xvärdenförstalagmtiter.append(temp[1])
    #hämta in stalagmtiter på fint sätt
#print(stalagmtiter)
xvärdenförstalagmtiter = sorted(xvärdenförstalagmtiter)
for b in range(antalbrev):
    a, b, c, d = [int(x) for x in input().split()]
    if a <= c:
        frånx, fråny, tillx, tilly = a, b, c, d
    else:
        frånx, fråny, tillx, tilly = c, d, a, b
    #print(frånx, fråny, tillx, tilly)
    lasty = fråny
    ydist = 0
    xdist = abs(tillx-frånx)
    lasttype = None
    for xval in xvärdenförstalagmtiter:
        if xval < frånx:
            continue
        elif xval > tillx:
            break
        else:
            yvärde = stalagmtiter[xval][1]
            typ = stalagmtiter[xval][0]
            if (lasttype == 1 and typ == 1 and yvärde <= lasty) or (lasttype == 2 and typ == 2 and yvärde >= lasty):
                continue
            elif (typ == 1 and yvärde > lasty) or (typ == 2 and yvärde < lasty):
                ydist += abs(lasty- yvärde)
                lasty = yvärde
                lasttype  = typ
    ydist += abs(lasty-tilly)
    print(ydist+xdist)
    #beräkna avståndet för det brevet