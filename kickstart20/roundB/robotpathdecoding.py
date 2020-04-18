from collections import deque
testcases = int(input())
for testcase in range(1, testcases+1):
    instruction = deque([char for char in input()][::-1])
    xpos = 0
    ypos = 0
    multipliers = [1]
    multiplier = 1
    while instruction:
        char = instruction.pop()
        if char == "E":
            xpos = (xpos + multiplier) % 1000000000
            continue
        elif char == "W":
            xpos = (xpos - multiplier) % 1000000000
            continue
        elif char == "N":
            ypos = (ypos - multiplier) % 1000000000
            continue
        elif char == "S":
            ypos = (ypos + multiplier) % 1000000000
            continue
        elif char == ")":
            last = multipliers.pop(-1)
            multiplier = 1
            for x in multipliers:
                multiplier *= x
            continue
        elif char == "(":
            continue
        elif char.isdigit(): # måste vara ett nummer,
            multipliers.append(int(char))
            multiplier = 1
            for x in multipliers:
                multiplier *= x
            continue
    print("Case #{}: {} {}".format(testcase, int(xpos+1), int(ypos+1)))