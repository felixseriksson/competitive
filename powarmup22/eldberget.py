from collections import deque
import sys
input = sys.stdin.readline

r, c, k = [int(a) for a in input().strip().split()]
grid = [["!" for _ in range(c+2)]]
for _ in range(r):
    grid.append(["!"] + [char for char in input().strip()] + ["!"])
grid.append(["!" for _ in range(c+2)])

dist = [[[-1 for _ in range(c+2)] for _ in range(r+2)] for _ in range(k+1)]

q = deque([(0,1,1)])
dist[0][1][1] = 0

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
while q:
    cur = q.popleft()
    fc, c1, c2 = cur[0], cur[1], cur[2]
    d = dist[fc][c1][c2]
    for o1, o2 in dirs:
        # if c1+o1 == r and c2+o2 == c:
        #     print(d+1)
        #     exit()
        if grid[c1+o1][c2+o2] == "." and dist[fc][c1+o1][c2+o2] == -1:
            dist[fc][c1+o1][c2+o2] = d+1
            q.append((fc, c1+o1, c2+o2))
        elif grid[c1+o1][c2+o2] == "#" and fc < k:
            if dist[fc+1][c1+o1][c2+o2] == -1:
                dist[fc+1][c1+o1][c2+o2] = d+1
                q.append((fc+1, c1+o1, c2+o2))

# for i in range(k+3):
#     for row in grid[i]:
#         print("".join([str(a) for a in row]))
#     print()

nums = [dist[i][-2][-2] for i in range(k+1)]
nums = [a for a in nums if a >= 0]
try:
    print(min(nums))
except:
    print("nej")
# print("nej")