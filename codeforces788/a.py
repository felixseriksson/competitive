for case in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    negs = len([c for c in l if c < 0])
    lpos = [c if c >= 0 else -c for c in l]
    for i in range(negs):
        lpos[i] *= -1
    if sorted(lpos) == lpos:
        print("YES")
    else:
        print("NO")