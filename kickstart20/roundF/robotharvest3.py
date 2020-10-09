from collections import deque
from math import ceil
cases = int(input())
for case in range(1, cases + 1):
    deployments = 0
    num, timebeforecal = [int(x) for x in input().split()]
    intervals = sorted([[int(x) for x in input().split()] for _ in range(num)])
    intervals = deque(intervals)
    start = intervals[0][0]
    stop = start + timebeforecal
    while intervals:
        nextint = intervals.popleft()
        neededforint = ceil((nextint[1] - nextint[0])/timebeforecal)
    print("Case #{}: {}".format(case, deployments))