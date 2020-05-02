from collections import OrderedDict
testcases = int(input())

for testcase in range(1, testcases+1):
    pancakesnum, dinersnum = [int(x) for x in input().split()]
    pancakes = [int(x) for x in input().split()]
    pancakedict = dict()
    for pc in pancakes:
        pancakedict[pc] = pancakes.count(pc)
    pancakes = sorted(list(dict.fromkeys(pancakes)))
    for i in range(pancakesnum):
        p = pancakes[i]
        cutsneeded = 0
        peopletoserve = dinersnum - pancakedict[p]
        # tempcakes = pancakes[::]
        # tempcakedict = dict(pancakedict)
        # for i in tempcakes:
        #     if i % p == 0:
        #         factor = i/p
        #         if factor <= peopletoserve:
        #             cutsneeded += factor - 1
        #             peopletoserve -= factor
        #         else:
        #             cutsneeded += factor
        #     else:
        #         continue
        factor = 1
        while peopletoserve > 0:
            try:
                number = pancakedict[factor*p]
                for num in range(number):
                    if peopletoserve >= factor:
                        peopletoserve -= factor
                        cutsneeded += factor-1
                    elif peopletoserve < factor:
                        cutsneeded += peopletoserve -1
                        peopletoserve = 0
            except:
                factor += 1
                continue
        
    print("Case #{}: {}".format(testcase, cutsneeded))