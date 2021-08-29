from collections import defaultdict

n = int(input())
colour = [int(x) for x in input().split()] # colour[i] = colour of node i
colour = [i if i == 1 else -1 for i in colour] # == 1 (white), == -1 (black)
graph = defaultdict(list)
for _ in range(n-1):
    a, b = [int(x) for x in input().split()]
    a, b = a-1, b-1
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, parent):
    dp[node] = colour[node]
    for ch in graph[node]:
        if ch == parent:
            continue
        dfs(ch, node)
        dp[node] += max(0, dp[ch])

dp = [0]*n
dfs(0, -1)