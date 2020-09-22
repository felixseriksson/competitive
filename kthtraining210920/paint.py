from collections import deque
n, k = [int(x) for x in input().split()]
subranges = deque()
for _ in range(k):
    subranges.append(tuple(int(x) for x in input().split()))

subranges = sorted(subranges, key = lambda x: x[1])
print(subranges)

# def mincovering(current, mustendafter):
#     if current < 0:
#         if mustendafter == 0:
#             return 0 # no more intervals needed
#         else:
#             return float("inf") # doesn't cover
        
#     if subranges[current][1] < mustendafter:
#         return float("inf") # doesn't cover
    
#     return min(1 + mincovering(current -1, subranges[current][0]), mincovering(current-1, mustendafter))

# print(mincovering(k, 0))