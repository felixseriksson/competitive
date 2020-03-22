testcases = int(input())

for n in range(1, testcases+1):
    stacks, platesperstack, platestopick = [int(x) for x in input().split()]
    stackslist = []
    for n in range(stacks):
        stackslist.append([int(x) for x in input().split()])
    maxstacks = [[]*stacks]
    fromeach = int(platestopick/stacks)
    rest = platestopick-fromeach*stacks
    for index in range(stacks):
        for x in range(fromeach):
            maxstacks[index].insert(0, stackslist[index].pop(0))
    for n in range(rest):
        pass