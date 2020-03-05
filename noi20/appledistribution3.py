from math import floor

def gethousesinrange(radius):
    points = 0
    for h in range(radius):
        points += floor((radius**2-h**2)**0.5)
    return 4*points + 1

def removedif(ones, fives):
    return sum([gethousesinrange(r) for r in oneresiduals[:ones]]) + sum([gethousesinrange(s) for s in fiveresiduals[:fives]])

rads = int(input())

radii = [int(x) for x in input().split()]
radii.sort()

rest = [1]
counter = 1
current = 1

for n in range(radii[-1]):
    if counter*(2**0.5)< n + 1:
        rest.append(current)
        counter += 1
    else:
        if current == 1:
            current = 5
        else:
            current = 1
        rest.append(current)

oneresiduals = []
fiveresiduals = []
onerescounter = 0
fiverescounter = 0
totrest = 0

for radius in radii:
    totrest += rest[radius]
    if onerescounter == 8 and fiverescounter == 8:
        break
    if onerescounter < 8 and rest[radius] == 1:
        oneresiduals.append(radius)
    if fiverescounter < 8 and rest[radius] == 5:
        fiveresiduals.append(radius)

totrest %= 8
len1 = len(oneresiduals)
len5 = len(fiveresiduals)

if totrest == 0:
    removed = 0
elif totrest == 1:
    if (len1 >= 0 and len5 >= 5) or (len1 >= 1 and len5 >= 0):
        removed = float("inf")
        if len1 >= 0 and len5 >= 5:
            removed = min(removed, removedif(0, 5))
        if len1 >= 1 and len5 >= 0:
            removed = min(removed, removedif(1, 0))
    else:
        removed = sum([gethousesinrange(r) for r in radii])
elif totrest == 2:
    if (len1 >= 0 and len5 >= 2) or (len1 >= 2 and len5 >= 0):
        removed = float("inf")
        if len1 >= 0 and len5 >= 2:
            removed = min(removed, removedif(0,2))
        if len1 >= 2 and len5 >= 0:
            removed = min(removed, removedif(2,0))
    else:
        removed = sum([gethousesinrange(r) for r in radii])
elif totrest == 3:
    if (len1 >= 0 and len5 >= 7) or (len1 >= 3 and len5 >= 0) or (len1 >= 1 and len5 >= 2):
        removed = float("inf")
        if len1 >= 0 and len5 >= 7:
            removed = min(removed, removedif(0, 7))
        if len1 >= 3 and len5 >= 0:
            removed = min(removed, removedif(3,0))
        if len1>= 1 and len5 >= 2:
            removed = min(removed, removedif(1,2))
    else:
        removed = sum([gethousesinrange(r) for r in radii])
elif totrest == 4:
    if (len1 >= 0 and len5 >= 4) or (len1 >= 4 and len5 >= 0) or (len1 >= 2 and len5 >= 2):
        removed = float("inf")
        if len1 >= 0 and len5 >= 4:
            removed = min(removed, removedif(0,4))
        if len1 >= 4 and len5 >= 0:
            removed = min(removed, removedif(4,0))
        if len1 >= 2 and len5 >= 2:
            removed = min(removed, removedif(2,2))
    else:
        removed = sum([gethousesinrange(r) for r in radii])
elif totrest == 5:
    if (len1 >= 0 and len5 >= 1) or (len1 >= 5 and len5 >= 0):
        removed = float("inf")
        if len1 >= 0 and len5 >= 1:
            removed = min(removed, removedif(0,1))
        if len1 >= 5 and len5 >= 0:
            removed = min(removed, removedif(5,0))
    else:
        removed = sum([gethousesinrange(r) for r in radii])
elif totrest == 6:
    if (len1 >= 0 and len5 >= 6) or (len1 >= 6 and len5 >= 0) or (len1 >= 1 and len5 >= 1):
        removed = float("inf")
        if len1 >= 0 and len5 >= 6:
            removed = min(removed, removedif(0,6))
        if len1 >= 6 and len5 >= 0:
            removed = min(removed, removedif(6,0))
        if len1 >= 1 and len5 >= 1:
            removed = min(removed, removedif(1,1))
    else:
        removed = sum([gethousesinrange(r) for r in radii])
elif totrest == 7:
    if (len1 >= 0 and len5 >= 3) or (len1 >= 7 and len5 >= 0) or (len1 >= 2 and len5 >= 1):
        removed = float("inf")
        if len1 >= 0 and len5 >= 3:
            removed = min(removed, removedif(0,3))
        if len1 >= 7 and len5 >= 0:
            removed = min(removed, removedif(7,0))
        if len1 >= 2 and len5 >= 1:
            removed = min(removed, removedif(2,1))
    else:
        removed = sum([gethousesinrange(r) for r in radii])

print(removed)

# if totrest == 0:
#     remove = 0
# elif totrest == 1:
#     possibilities = []
#     if len1 >= 1:
#         possibilities.append(gethousesinrange(oneresiduals[0]))
#     if len5 >= 5:
#         possibilities.append(sum([gethousesinrange(r) for r in fiveresiduals[:5]]))
#     if len1 < 1 and len5 < 5:
#         temp = 0
#         for rad in radii:
#             temp += gethousesinrange(rad)
#         possibilities.append(temp)
#     remove = min(possibilities)
# elif totrest == 2:
#     possibilities = []
#     if len1 >= 2:
#         possibilities.append(sum([gethousesinrange(r) for r in oneresiduals[:2]]))
#     if len5 >= 2:
#         possibilities.append(sum([gethousesinrange(r) for r in fiveresiduals[:2]]))
#     if len1 < 2 and len5 < 2:
#         temp = 0
#         for rad in radii:
#             temp += gethousesinrange(rad)
#         possibilities.append(temp)
#     remove = min(possibilities)
# elif totrest == 3:
#     possibilities = []
#     if len1 >= 3:
#         possibilities.append(sum([gethousesinrange(r) for r in oneresiduals[:3]]))
#     if len5 >= 7:
#         possibilities.append(sum([gethousesinrange(r) for r in fiveresiduals[:7]]))
#     if len1 >= 1 and len5 >= 2:
#         possibilities.append([gethousesinrange(r) for r in oneresiduals[0] ]+ sum([gethousesinrange(r) for r in fiveresiduals[:2]]))
#     if len1 < 3 and len5 < 7:
#         temp = 0
#         for rad in radii:
#             temp += gethousesinrange(rad)
#         possibilities.append(temp)
#     remove = min(possibilities)
# elif totrest == 4:
#     possibilities = []
#     if len1 >= 4:
#         possibilities.append(sum([gethousesinrange(r) for r in oneresiduals[:4]]))
#     if len5 >= 4:
#         possibilities.append(sum([gethousesinrange(r) for r in fiveresiduals[:4]]))
#     if len1 >= 2 and len5 >= 2:
#         possibilities.append(sum([gethousesinrange(r) for r in oneresiduals[:2]] + sum([gethousesinrange(r) for r in fiveresiduals[:2]])))
#     if (len1 < 2 and len5 < 2) or (len1 < 4 and len5 == 1) or (len1 == 1 and len5 < 4):
#         temp = 0
#         for rad in radii:
#             temp += gethousesinrange(rad)
#         possibilities.append(temp)
#     remove = min(possibilities)
# elif totrest == 5:
#     possibilities = []
#     if len1 >= 5:
#         possibilities.append(sum([gethousesinrange(r) for r in oneresiduals[:5]]))
#     if len5 >= 1:
#         possibilities.append(gethousesinrange(fiveresiduals[0]))
#     if len1 < 5 and len5 < 1:
#         temp = 0
#         for rad in radii:
#             temp += gethousesinrange(rad)
#         possibilities.append(temp)
#     remove = min(possibilities)
# elif totrest == 6:
#     possibilities = []
#     if len1 >= 6:
#         possibilities.append(sum([gethousesinrange(r) for r in oneresiduals[:6]]))
#     if len5 >= 6:
#         possibilities.append(sum([gethousesinrange(r) for r in fiveresiduals[:6]]))
#     if len1 >= 1 and len5 >= 1:
#         possibilities.append(gethousesinrange(oneresiduals[0]) + gethousesinrange(fiveresiduals[0]))
#     if (len1 < 1 and len5 < 5) or (len1 < 6 and len5 == 0) or ( len1 == 0 and len5 < 6):
#         temp = 0
#         for rad in radii:
#             temp += gethousesinrange(rad)
#         possibilities.append(temp)
#     remove = min(possibilities)
# elif totrest == 7:
#     possibilities = []
#     if len1 >= 7:
#         possibilities.append(sum([gethousesinrange(r) for r in oneresiduals[:7]]))
#     if len5 >= 3:
#         possibilities.append(sum([gethousesinrange(r) for r in fiveresiduals[:3]]))
#     if len1 >= 2 and len5 >= 1:
#         possibilities.append(sum([gethousesinrange(r) for r in oneresiduals[:2]]) + gethousesinrange(fiveresiduals[0]))
#     if (len1 < 2 and len5 == 0) or (len1 < 7 and len5 == 0) or ( len1 < 2 and len5 < 3):
#         temp = 0
#         for rad in radii:
#             temp += gethousesinrange(rad)
#         possibilities.append(temp)
#     remove = min(possibilities)

# print(remove)