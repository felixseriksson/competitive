# for case in range(1, int(input())+1):
#     n, cost = [int(x) for x in input().split()]
#     if cost < n-1 or cost > (n**2+n)/2 - 1:
#         print("Case #{}: IMPOSSIBLE".format(case))
#         continue
#     excess = cost - n + 1
#     l = list(range(1, n+1))
#     for lower in range(0, n-1):
#         if excess >= n - lower - 1:
#             l[lower:] = list(reversed(l[lower:]))
#             excess -= (n - lower - 1)
#     s = " ".join([str(char) for char in l])
#     print("Case #{}: {}".format(case, s))

for case in range(1, int(input())+1):
    n, cost = [int(x) for x in input().split()]
    if cost < n-1 or cost > (n**2+n)/2 - 1:
        print("Case #{}: IMPOSSIBLE".format(case))
        continue
    
    l = [1 for _ in range(n-1)]
    excess = cost - n + 1
    for i in range(n):
        if not excess:
            break
        else:
            l[i] += min(excess, i+1)
            excess -= min(excess, i+1)


    reverselist = list(range(1, n+1))
    for i in range(len(l)):
        lower = n - i - 2
        offset = lower + l[i]
        reverselist = reverselist[:lower] + list(reversed(reverselist[lower:offset])) + reverselist[offset:]

    s = " ".join([str(char) for char in reverselist])
    print("Case #{}: {}".format(case, s))