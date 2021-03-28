n, k = [int(x) for x in input().split()]
d, s = [int(x) for x in input().split()]
ret = (d*n - k*s)/(n - k)
if ret < 0 or ret > 100:
    ret = "impossible"
print(ret)