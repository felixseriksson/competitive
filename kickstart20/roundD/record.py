from collections import deque
cases = int(input())
for case in range(1, cases+1):
    ctr = 0
    numdays = int(input())
    days = deque([int(x) for x in input().split()])
    maxd = -1
    day1 = days.popleft()
    for _ in range(numdays-1):
        day2 = days.popleft()
        if day1 > maxd:
            maxd = day1
            if day1 > day2:
                ctr += 1
        day1 = day2
    if day1 > maxd:
        ctr += 1
    print("Case #{}: {}".format(case, ctr))