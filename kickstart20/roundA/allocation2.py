testcases = int(input())

for n in range(1, testcases+1):
    l1 = [int(x) for x in input().split()]
    houses = l1[0]
    budget = l1[1]
    prices = [int(x) for x in input().split()]
    prices.sort()
    number = 0
    while True:
        if len(prices) == 0:
            break
        nexthouse = prices.pop(0)
        if budget >= nexthouse:
            budget -= nexthouse
            number += 1
        else:
            break
    print("Case #{}: {}".format(n, number))
