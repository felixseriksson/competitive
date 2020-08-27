a, b, c, n = [int(x) for x in input().split()]
'''
totprobs = a + b + c
made = False
if totprobs >= n:
    if a > 0:
        if b > 0:
            if c > 0:
                print("YES")
                made = True
if made == False:
    print("NO")
'''
can = False
if a > 0:
    n -= min(a, n-2)
    if b > 0:
        n -= min(b, n-1)
        if c > 0:
            n -= min(c, n)
            can = True
if can == True and n == 0:
    print("YES")
else:
    print("NO")