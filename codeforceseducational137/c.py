for _ in range(int(input())):
    n = int(input())
    bitmask = [int(x) for x in input()]
    arr = [int(x) for x in input().split()]
    if not 0 in bitmask:
        print(sum(arr))
        continue
    else:
        firstzeroidx = bitmask.index(0)
        ret = sum(arr[:firstzeroidx])
        bitmask = bitmask[firstzeroidx:]
        arr = arr[firstzeroidx:]
        n = n - firstzeroidx
        startindex, stopindex = [], []
        for i in range(n - 1):
            if bitmask[i] == 0 and bitmask[i + 1] == 1:
                startindex.append(i)
            elif bitmask[i] == 1 and bitmask[i + 1] == 0:
                stopindex.append(i + 1)
        if len(startindex) > len(stopindex):
            stopindex.append(n)
        elif len(startindex) < len(stopindex):
            startindex.insert(0, 0)
            
        for i, j in zip(startindex, stopindex):
            ret += sum(arr[i:j])
            ret -= min(arr[i:j])
        print(ret)