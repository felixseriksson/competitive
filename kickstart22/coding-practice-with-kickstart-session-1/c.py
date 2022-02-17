for i in range(int(input())):
    n, l = int(input()), [int(x) for x in input().split()]
    c, h, extra, output = [0 for _ in range(n+1)], 0, 0, []
    for k in l:
        if k > h:
            c[min(n, k)] += 1
            if extra == c[h]:
                h += 1
                extra = 0
            else:
                extra += 1

        output.append(h)
    print(f'Case #{i+1}: {" ".join([str(a) for a in output])}')