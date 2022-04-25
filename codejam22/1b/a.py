from collections import deque

for case in range(1, int(input()) + 1):
    n = int(input())
    d = deque([int(x) for x in input().split()])
    ans, maxseen = 0, 0
    while d:
        if d[0] <= d[-1]:
            if d[0] >= maxseen:
                ans += 1
            maxseen = max(maxseen, d.popleft())
        else:
            if d[-1] >= maxseen:
                ans += 1
            maxseen = max(maxseen, d.pop())


    print(f"Case #{case}: {ans}")