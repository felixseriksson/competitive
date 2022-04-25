from random import sample

def getstring(n):
    idx = list(range(8))
    onesidx = set(sample(idx, n))
    ret = ["1" if i in onesidx else "0" for i in range(8)]
    return "".join(ret)

for case in range(1, int(input()) + 1):
    print(getstring(4), flush = True)
    response = int(input())
    while response != 0:
        if response == -1:
            exit()
        print(getstring(response), flush = True)
        response = int(input())