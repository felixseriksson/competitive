from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def gcd(a, b):
    a, b = max(a,b), min(a,b)
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return a*b//gcd(a,b)

MOD = 10**9 + 7

for _ in range(int(input())):
    b, q, y = [int(x) for x in input().split()]
    c, r, z = [int(x) for x in input().split()]
    # first sequence:  b, b + q, ..., b + y*q
    # second sequence: c, c + r, ..., c + z*r
    if c + (z-1)*r > b + (y-1)*q:
        print(0)
    elif c < b:
        print(0)
    elif r % q != 0:
        print(0)
    elif (c-b) % q != 0:
        print(0)
    # elif (c-b)//q < 0 or (c-b)//q > y:
    #     print(0)
    else:
        # possible, finitely or infinitely many times
        if c + z*r > b + (y-1)*q or c - r < b:
            # infinitely
            print(-1)
        else:
            # finitely
            res = 0
            for p in factors(r):
                if lcm(p, q) == r:
                    res = (res + (r//p)**2) % MOD
            print(res)