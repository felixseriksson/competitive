n, c = [int(x) for x in input().split()]
xs = [int(x) for x in input().split()]
print(0, end=" ")
y1 = max(-xs[0], -xs[1] + c)
y2 = max(xs[0], xs[1] + c)
for i in range(1, n):
    y1 = max(y1, -xs[i] + c*i)
    y2 = max(y2, xs[i] + c*i)
    s1 = xs[i] - c*i + y1
    s2 = -xs[i] - c*i + y2
    print(max(s1, s2), end=" ")