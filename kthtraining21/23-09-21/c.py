from collections import deque
n = int(input())
bears = [int(x) for x in input().split()]
bears.insert(0, 0)
bears.append(0)
l = []
r = []
q = deque()
for i in range(1, n+1):
    try:
        while bears[q[-1]] >= bears[i]:
            q.pop()
    except:
        pass
    try:
        l.append(q[-1])
    except:
        l.append(0)
    q.append(i)
q = deque()
for i in range(1, n+1):
    try:
        while bears[q[-1]] <= bears[i]:
            q.pop()
    except:
        pass
    try:
        l.append(q[-1])
    except:
        l.append(n+1)
    q.append(i)
print(r)