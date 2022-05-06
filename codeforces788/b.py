for _ in range(int(input())):
    n = int(input())
    string = input()
    k, *rest = input().split()
    rest = set(rest)
    l = ["b" if c in rest else "a" for c in string]
    try:
        bindex = l[::-1].index('b')
        l = l[:n - bindex]
        n -= bindex
    except:
        pass
    # lset = set(l)
    # if len(lset) == 1:
    #     if "a" in lset:
    #         print(0)
    #     else:
    #         if len(l) == 1:
    #             print(0)
    #         else:
    #             print(1)
    if n == 1:
        print(0)
    else:
        cnt = 0
        mmax = 0
        curr = 0
        startedflag = False
        for i in range(n):
            if startedflag:
                if l[i] == "a":
                    curr += 1
                else:
                    cnt += 1
                    mmax = max(mmax, curr)
                    startedflag = False
                    curr = 0
            else:
                if l[i] == "a":
                    curr += 1
                    startedflag = True
                else:
                    continue
        if cnt <= 1:
            if "a" in l:
                print(mmax)
            else:
                print(1)
        else:
            print(mmax + 1)