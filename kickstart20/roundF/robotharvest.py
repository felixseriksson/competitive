# # from collections import deque
# from heapq import heappush, heappop, heapify
# cases = int(input())
# for case in range(1, cases + 1):
#     deployments = 0
#     num, timebeforecal = [int(x) for x in input().split()]
#     intervals = []
#     for _ in range(num):
#         intervals.append([int(x) for x in input().split()])
#     # intervals = deque(sorted(intervals))
#     # # print(intervals)
#     # while intervals:
#     #     deployments += 1
#     #     start = intervals[0][0]
#     #     stop = start + timebeforecal
#     #     for interval in list(intervals)[:]:
#     #         if interval[1] <= stop: # kan göra helt
#     #             del intervals[intervals.index(interval)]
#     #         elif interval[0] < stop: # kan göra delvis
#     #             intervals[intervals.index(interval)][0] = stop
#     #         else: # kan inte göra över huvud taget
#     #             break
#     heapify(intervals)
#     while intervals:
#         deployments += 1
#         start = intervals[0][0]
#         stop = start + timebeforecal
#         goon = True
#         while goon:
#             try:
#                 current = heappop(intervals)
#             except:
#                 break
#             if current[1] <= stop:
#                 continue
#             elif current[0] <= stop:
#                 current[0] = stop
#                 heappush(intervals, current)
#                 goon = False
#             else:
#                 goon = False
#                 heappush(intervals, current)
#     print(f"Case #{case}: {deployments}")
#-----------------------------------------------
from collections import deque
cases = int(input())
for case in range(1, cases + 1):
    deployments = 0
    n, k = [int(x) for x in input().split()]
    intervals = sorted([tuple(int(x) for x in input().split()) for _ in range(n)])
    intervals = deque(intervals)
    while intervals:
        start = intervals[0][0]
        stop = start + k
        deployments += 1
        while True:
            try:
                curr = intervals.popleft()
            except IndexError:
                break
            if curr[0] <= start and curr[1] <= stop:
                start = curr[1]
                continue
            elif curr[0] <= stop and curr[1] > stop:
                curr = (stop, curr[1])
                intervals.appendleft(curr)
                break
            elif curr[0] > stop:
                intervals.appendleft(curr)
                break
    print(f"Case #{case}: {deployments}")
#----------------------------------------------
# cases = int(input())
# for case in range(1, cases + 1):
#     deployments = 0
#     n, k = [int(x) for x in input().split()]
#     intervals = sorted([tuple(int(x) for x in input().split()) for _ in range(n)])
#     while intervals:
#         deployments += 1
#         start = intervals[0][0]
#         stop = start + k
#         intervals = list(filter(lambda x: x[1] > stop, intervals))
#         if intervals:
#             if intervals[0][0] <= stop:
#                 intervals[0] = (stop, int(intervals[0][1]))
#     print(f"Case #{case}: {deployments}")