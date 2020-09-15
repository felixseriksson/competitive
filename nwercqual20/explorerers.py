# from collections import Counter
# from math import floor, ceil
# cases = int(input())
# for _ in range(cases):
#     num = int(input())
#     levels = Counter(sorted([int(x) for x in input().split()]))
#     teams = 0
#     left = 0
#     for val in levels.keys():
#         teams += floor((levels[val] + left)/val)
#         left = (levels[val] + left)%val


#     # kvar = sorted(levels.elements(), reverse=True)
#     # team = []
#     # while kvar:
#     #     last = kvar.pop(-1)
#     #     team.append(last)
#     #     if len(team) == last:
#     #         teams += 1
#     #         team = []
#     print(teams)

from collections import Counter
cases = int(input())
for _ in range(cases):
    num = int(input())
    levels = Counter([int(x) for x in input().split()])
    teams = 0
    left = 0
    for key in sorted(levels.keys()):
        levels[key]+= left
        teams += levels[key]//key
        left = levels[key] % key
    print(teams)

# from collections import Counter
# cases = int(input())
# for _ in range(cases):
#     num = int(input())
#     tmp = [int(x) for x in input().split()]
#     levels = [0]*(max(tmp))
#     for exp in tmp:
#         levels[exp] += 1
#     teams = 0
#     left = 0
#     for exp in range(max(tmp)):
#         levels[exp] += left
#         teams += levels[exp]//exp
#         left = levels[exp]//exp
#         levels[key]+= left
#         teams += levels[key]//key
#         left += levels[key] % key
#     print(teams)