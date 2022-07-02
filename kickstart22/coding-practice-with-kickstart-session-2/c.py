for case in range(1, int(input()) + 1):
    n, q = [int(x) for x in input().split()]
    s = [ord(x) - 65 for x in input()]
    pref = [[0 for _ in range(n+1)] for _ in range(26)]
    for idx, char in enumerate(s):
        for i in range(26):
            if i == char:
                pref[i][idx + 1] = pref[i][idx] + 1
            else:
                pref[i][idx + 1] = pref[i][idx]

    ans = 0
    for _ in range(q):
        l, r = [int(x) for x in input().split()]
        numodds = 0
        for i in range(26):
            if (pref[i][r] - pref[i][l-1]) % 2:
                numodds += 1
        if numodds == 0 or numodds == 1:
            ans += 1
    print(f"Case #{case}: {ans}")