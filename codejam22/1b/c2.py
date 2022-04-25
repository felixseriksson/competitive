from random import sample

def getstring(n):
    idx = list(range(8))
    onesidx = set(sample(idx, n))
    ret = ["1" if i in onesidx else "0" for i in range(8)]
    return "".join(ret)

for case in range(1, int(input()) + 1):
    print(getstring(1), flush = True)
    response = input()
    while response != 0:
        if response == "-1":
            exit()
        elif response == "8":
            print("11111111")
        else:
            print(getstring(1), flush = True)
        response = input()
