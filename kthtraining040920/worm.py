# from math import ceil
# up, down, length = [int(x) for x in input().split()]
# beforelast = length - up
# perclimb = up - down
# times = ceil(beforelast/perclimb)
# print(times + 1)
up, down, length = [int(x) for x in input().split()]
climbed = 0
ctr = 0
while climbed < length:
    climbed += up
    ctr += 1
    if climbed >= length:
        break
    else:
        climbed -= down
print(ctr)