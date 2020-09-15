cases = int(input())
for case in range(cases):
    length = int(input())
    ls = [int(x) for x in input().split()]
    mask = [int(x) for x in input().split()]
    openlist = [ls[k] for k in range(len(ls)) if not mask[k]]
    openlist.sort(reverse=True)
    newlist = []
    for index in range(len(mask)):
        if mask[index]:
            newlist.append(ls[index])
        else:
            newlist.append(openlist.pop(0))
    print(" ".join([str(val) for val in newlist]))