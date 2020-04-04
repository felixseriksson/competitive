testcases = int(input())
for testcase in range(1, testcases+1):
    n = int(input())
    ranges = []
    C = -1
    J = -1
    for activity in range(n):
        start, stop = [int(x) for x in input().split()]
        ranges.append((start, stop, "Astart", activity))
        ranges.append((stop, stop, "Bstop"))

    ranges = sorted(ranges)
    broke = False
    activities = [None]*n
    for i in ranges:
        if i[2] == "Astart":
            if C == -1:
                C = i[1]
                activities[i[3]] = "C"
            elif J == -1:
                J = i[1]
                activities[i[3]] = "J"
            else:
                broke = True
                break
        elif i[2] == "Bstop":
            if C == i[1]:
                C = -1
            elif J == i[1]:
                J = -1
    
    final = "IMPOSSIBLE" if broke else "".join(activities)
    
    print("Case #{}: {}".format(testcase, final))