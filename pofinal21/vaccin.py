N, Q = [int(x) for x in input().split()]
days = [int(x) for x in input().split()]
d = []
for index, day in enumerate(days):
    for _ in range(day):
        d.append(index+1)
# print(d)
for q in [int(x) for x in input().split()]:
    try:
        print(d[q])
    except:
        print(-1)