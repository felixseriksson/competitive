n = int(input())
first = [int(x) for x in input().split()]
second = [int(x) for x in input().split()]
third = [int(x) for x in input().split()]
firstcopy = first[:]
secondcopy = second[:]

def twicetrianglearea(a, b, c):
    return abs(a[0]*(b[1] - c[1]) + b[0]*(c[1] - a[1]) + c[0]*(a[1] - b[1]))

minarea = twicetrianglearea(first, second, third)
if minarea == 0:
    minarea = float("inf")

for _ in range(n-3):
    first, second, third = second, third, [int(x) for x in input().split()]
#     print(twicetrianglearea(first, second, third)
    area = twicetrianglearea(first, second, third)
    if area != 0:
        minarea = min(minarea, twicetrianglearea(first, second, third))

# print(twicetrianglearea(second, third, firstcopy))
# print(twicetrianglearea(third, firstcopy, secon))
t1 = twicetrianglearea(second, third, firstcopy)
t2 = twicetrianglearea(third, firstcopy, secondcopy)
if t1 != 0:
    minarea = min(minarea, t1)
if t2 != 0:
    minarea = min(minarea, t2)

print(minarea)