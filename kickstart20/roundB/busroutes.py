from collections import deque
testcases = int(input())
for testcase in range(1, testcases+1):
    buses, arrivalday  = [int(x) for x in input().split()]
    reversedlist = deque([int(x) for x in input().split()])
    currday = arrivalday
    while reversedlist:
        nextone = reversedlist.pop()
        currday = (currday // nextone)*nextone
    print("Case #{}: {}".format(testcase,currday))