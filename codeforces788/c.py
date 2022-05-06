MOD = 10**9+7

for _ in range(int(input())):
    n = int(input())
    # idx to number
    a, b, c = dict(), dict(), dict()

    # number to idx
    arev, brev, crev = dict(), dict(), dict()
    for idx, num in enumerate([int(x) for x in input().split()], start = 1):
        a[idx] = num
        arev[num] = idx
    for idx, num in enumerate([int(x) for x in input().split()], start = 1):
        b[idx] = num
        brev[num] = idx
    for idx, num in enumerate([int(x) for x in input().split()], start = 1):
        if num != 0:
            c[idx] = num
            crev[num] = idx

    seen = set()
    for num in list(c.values())[::]:
        curr = num
        while not curr in seen:
            seen.add(curr)
            curridx = crev[curr]
            aatcurridx = a[curridx]
            batcurridx = b[curridx]
            if aatcurridx == curr:
                forced = batcurridx
                forcedidx = arev[forced]
            else:
                forced = aatcurridx
                forcedidx = brev[forced]
            c[forcedidx] = forced
            crev[forced] = forcedidx
            curr = forced
    
    ret = 1
    for i in range(1, n+1):
        if i in seen:
            continue
        else:
            cyclelength = 1
            seen.add(i)
            while not b[arev[i]] in seen:
                i = b[arev[i]]
                seen.add(i)
                cyclelength += 1
            if cyclelength > 1:
                ret *= 2
            ret %= MOD
    print(ret)