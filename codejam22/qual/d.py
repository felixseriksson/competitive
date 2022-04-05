def solve(node):
    if len(prev[node]) == 0:
        return val[node]
    else:
        returns = []
        for p in prev[node]:
            returns.append(solve(p))
        minval = min(returns)

        if val[node] <= minval:
            return sum(returns)
        else:
            return sum(returns) + val[node] - minval

for case in range(1, int(input())+1):
    n = int(input())
    val, prev = dict(), dict()
    terminals = set()
    for node, v in enumerate([int(x) for x in input().split()], start = 1):
        val[node] = v
        prev[node] = []
    for p, node in enumerate([int(x) for x in input().split()], start = 1):
        if node == 0:
            terminals.add(p)
        else:
            prev[node].append(p)

    total = 0
    for t in terminals:
        total += solve(t)
    print(f"Case #{case}: {total}")

# def solve(node):
#     if len(prev[node]) == 0:
#         return (val[node], val[node])
#     else:
#         returns = []
#         for p in prev[node]:
#             returns.append(solve(p))
#         minval = 10**9
#         mini = 0
#         for i in range(len(returns)):
#             if returns[i][1] < minval:
#                 mini = i
#                 minval = returns[i][1]

#         if val[node] <= minval:
#             ssum = sum([x[0] for x in returns])
#             return (ssum, val[node])
#         else:
#             returns[mini][1] = val[node]