from math import floor

def gethousesinrange(radius):
    points = 0
    for h in range(radius):
        points += floor((radius**2-h**2)**0.5)
    return 4*points + 1

rads = int(input())
applesdelivered = [gethousesinrange(int(x)) for x in input().split()]
applesdelivered.sort()
oneresiduals = []
fiveresiduals = []
for el in applesdelivered:
    if el % 8 == 1:
        oneresiduals.append(el)
    elif el % 8 == 5:
        fiveresiduals.append(el)
summa = sum(applesdelivered)
totrest = summa % 8
len1 = len(oneresiduals)
len5 = len(fiveresiduals)

if totrest == 0:
    remove = 0
elif totrest == 1:
    possibilities = [summa]
    if len1 >= 1:
        possibilities.append(oneresiduals[0])
    if len5 >= 5:
        possibilities.append(sum(fiveresiduals[:5]))
    remove = min(possibilities)
elif totrest == 2:
    possibilities = [summa]
    if len1 >= 2:
        possibilities.append(sum(oneresiduals[:2]))
    if len5 >= 2:
        possibilities.append(sum(fiveresiduals[:2]))
    remove = min(possibilities)
elif totrest == 3:
    possibilities = [summa]
    if len1 >= 3:
        possibilities.append(sum(oneresiduals[:3]))
    if len5 >= 7:
        possibilities.append(sum(fiveresiduals[:7]))
    if len1 >= 1 and len5 >= 2:
        possibilities.append(oneresiduals[0] + sum(fiveresiduals[:2]))
    remove = min(possibilities)
elif totrest == 4:
    possibilities = [summa]
    if len1 >= 4:
        possibilities.append(sum(oneresiduals[:4]))
    if len5 >= 4:
        possibilities.append(sum(fiveresiduals[:4]))
    if len1 >= 2 and len5 >= 2:
        possibilities.append(sum(oneresiduals[:2] + sum(fiveresiduals[:2])))
    remove = min(possibilities)
elif totrest == 5:
    possibilities = [summa]
    if len1 >= 5:
        possibilities.append(sum(oneresiduals[:5]))
    if len5 >= 1:
        possibilities.append(fiveresiduals[0])
    remove = min(possibilities)
elif totrest == 6:
    possibilities = [summa]
    if len1 >= 6:
        possibilities.append(sum(oneresiduals[:6]))
    if len5 >= 6:
        possibilities.append(sum(fiveresiduals[:6]))
    if len1 >= 1 and len5 >= 1:
        possibilities.append(oneresiduals[0] + fiveresiduals[0])
    remove = min(possibilities)
elif totrest == 7:
    possibilities = [summa]
    if len1 >= 7:
        possibilities.append(sum(oneresiduals[:7]))
    if len5 >= 3:
        possibilities.append(sum(fiveresiduals[:3]))
    if len1 >= 2 and len5 >= 1:
        possibilities.append(sum(oneresiduals[:2]) + fiveresiduals[0])
    remove = min(possibilities)
print(remove)