def ways(n):
    return 1 if n == 0 else (n if (n == 1 or n == 2) else ways(n-1) + ways(n-2) + ways(n-3))
print(ways(int(input())))