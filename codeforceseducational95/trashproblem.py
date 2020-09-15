from bisect import insort
piles, queries = [int(x) for x in input().split()]
ls = sorted([int(x) for x in input().split()])
multisetish = [abs(ls[i]-ls[i+1]) for i in range(len(ls)-1)]
try:
    print(ls[-1] - ls[0] - max(multisetish))
except:
    print(0)
for _ in range(queries):
    q, coord = [int(x) for x in input().split()]
    if len(ls) == 2:
        if q == 0:
            ls.remove(coord)
            multisetish = []
        elif q == 1:
            ls.append(coord)
            ls = sorted(ls)
            multisetish = []
            multisetish.append(abs(ls[0] - ls[1]))
            multisetish.append(abs(ls[1] - ls[2]))
    elif len(ls) == 1:
        if q == 0:
            ls = []
        elif q == 1:
            ls.append(coord)
            ls = sorted(ls)
            multisetish.append(abs(ls[0] - ls[1]))
    elif len(ls) == 0:
        if q == 0:
            raise Exception
        # idk man can't remove items from an empty list
        elif q == 1:
            ls.append(coord)
    else:
        if q == 0:
            # remove
            ind = ls.index(coord)
            if ind == 0:
                multisetish.remove(abs(ls[0] - ls[1]))
            elif coord == ls[-1]:
                multisetish.remove(abs(ls[ind] - ls[ind-1]))
            else:
                multisetish.remove(abs(ls[ind] - ls[ind-1]))
                multisetish.remove(abs(ls[ind] - ls[ind+1]))
                multisetish.append(abs(ls[ind-1] - ls[ind+1]))
            ls.remove(coord)
        elif q == 1:
            # add
            insort(ls, coord)
            ind = ls.index(coord)
            if ind == 0:
                multisetish.append(abs(ls[ind] - ls[ind+1]))
            elif coord == ls[-1]:
                multisetish.append(abs(ls[ind] - ls[ind-1]))
            else:
                multisetish.append(abs(ls[ind] - ls[ind-1]))
                multisetish.append(abs(ls[ind] - ls[ind+1]))
                multisetish.remove(abs(ls[ind-1] - ls[ind+1]))
    try:
        print(ls[-1] - ls[0] - max(multisetish))
    except:
        print(0)