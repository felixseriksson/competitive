testcases = int(input())
for testcase in range(1, testcases+1):
    points = int(input())
    numpeaks = 0
    pointslist = [int(x) for x in input().split()]
    for i in range(1, points-1):
        if pointslist[i] > pointslist[i-1] and pointslist[i] > pointslist[i+1]:
            numpeaks += 1
    print("Case #{}: {}".format(testcase, numpeaks))