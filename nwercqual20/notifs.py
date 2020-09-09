inputs = int(input())
mins = 0
for _ in range(inputs):
    ti, dt = [int(x) for x in input().split()]
    mins = max(mins, ti) + dt

print(mins)