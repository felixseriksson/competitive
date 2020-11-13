stacks = int(input())
coins = [int(x) for x in input().split()]
coins = sorted([[a, b] for a, b in zip(coins, range(1, stacks+1))], key = lambda x: x[0], reverse = True)
ls = []
broke = False
while coins:
    try:
        assert coins[0][0] >= 1 and coins[-1][0] >= 1
    except:
        broke = True
        break
    ls.append("{} {}".format(coins[0][1], coins[-1][1]))
    coins[0][0] -= 1
    coins[-1][0] -= 1
    coins = sorted([coin for coin in coins if coin[0] != 0], key = lambda x: x[0], reverse = True)
if broke:
    print("no")
else:
    print("yes")
    print("\n".join(ls))