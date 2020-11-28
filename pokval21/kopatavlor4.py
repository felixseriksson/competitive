n, k = [int(x) for x in input().split()]
time = [int(x) for x in input().split()]

for window in range(k, n):
    iterationmin = float("inf")
    runningsum = sum(time[:k])
    for offset in range(n - k - 1):
        runningsum -= time[offset]