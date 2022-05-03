def check(maxa, mina):
    for a, b in zip(maxa, mina[1:]):
        if a > b:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    tmpa = [int(x) for x in input().split()]
    if not len(tmpa) % 2:
        maxa = [max(x, y) for x, y in zip(tmpa[::2], tmpa[1::2])]
        mina = [min(x, y) for x, y in zip(tmpa[::2], tmpa[1::2])]
    else:
        maxa = [tmpa[0]] + [max(x, y) for x, y in zip(tmpa[1::2], tmpa[2::2])]
        mina = [tmpa[0]] + [min(x, y) for x, y in zip(tmpa[1::2], tmpa[2::2])]
    # print(maxa)
    # print(mina)
    if check(maxa, mina):
        print("YES")
    else:
        print("NO")