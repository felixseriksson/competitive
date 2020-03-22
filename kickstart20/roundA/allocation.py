cases = int(input())
for n in range(1,cases+1):
    houses, budget = [int(x) for x in input().split()]
    prices = [int(x) for x in input().split()]
    prices.sort()
    ctr = 0
    while True:
        nextprice = prices.pop(0)
        if budget >= nextprice:
            budget -= nextprice
            ctr += 1
        else:
            break
    print("Case #{}: {}".format(n, ctr))