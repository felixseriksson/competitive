for case in range(1, int(input())+1):
    n = int(input())
    val = [-1] + [int(x) for x in input().split()]
    pointsat = [-1] + [int(x) for x in input().split()]
    nodes = sorted([i for i in range(n+1)], key = lambda x: pointsat[x], reverse = True)
    howmanypointat = [0]*(n+1)
    for p in pointsat[1:]:
        howmanypointat[p] += 1

    total, i = 0, 0
    while i < n+1:
        layer = nodes[i:i+howmanypointat[pointsat[nodes[i]]]]
        if pointsat[nodes[i]] == 0: 
            print(f"Case #{case}: {total + sum([val[node] for node in layer])}")
            break
        elif howmanypointat[pointsat[nodes[i]]] == 1:
            val[pointsat[nodes[i]]] = max(val[pointsat[nodes[i]]], val[nodes[i]])
            i += 1
            continue
        else:
            minval = min([val[node] for node in layer])
            total += sum([val[node] for node in layer]) - minval
            val[pointsat[nodes[i]]] = max(val[pointsat[nodes[i]]], minval)
            i += len(layer)