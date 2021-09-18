for case in range(1, int(input())+1):
    n = int(input())
    s = input()
    ret = 0
    if s[0] != "1":
        beg = s.index("1")
        ret += beg*(beg+1)//2
        s = s[beg:]
    if s[-1] != "1":
        end = s[::-1].index("1")
        ret += end*(end+1)//2
        s = s[:-end]
    s = s.split("1")
    s = [a for a in s if a != ""]
    for zeroes in s:
        if len(zeroes) % 2:
            steps = int(len(zeroes)//2)
            ret += steps*(steps+1)
            ret += steps+1
        else:
            steps = int(len(zeroes)/2)
            ret += steps*(steps+1)
    print(f"Case #{case}: {ret}")