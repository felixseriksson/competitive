def ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return ways(n-5) + ways(n-4) + ways(n-3) + ways(n-2)

print(ways(23)*2)