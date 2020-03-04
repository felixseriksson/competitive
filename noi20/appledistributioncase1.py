from math import floor

def gethousesinrange(radius):
    points = 0
    for h in range(radius):
        points += floor(((radius**2)-(h**2))**0.5)
    return 4*points + 1

vals = []

for n in range(301):
    vals.append(gethousesinrange(n))

rads = int(input())
applesdelivered = [gethousesinrange(int(x)) for x in input().split()]
applesdelivered.sort()

summa = 0
for n in applesdelivered:
    summa +=vals[n]

rest = summa % 8

if rest == 0:
    removed = 0
elif rest > 0 and rest <= 4:
    removed = 0
    counter = 0
    for n in applesdelivered:
        if n % 8 == 1:
            counter += 1
            removed += n
        if counter == rest:
            break
    