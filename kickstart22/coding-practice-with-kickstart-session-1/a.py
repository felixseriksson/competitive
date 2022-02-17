for i in range(int(input())):
    n, m = [int(x) for x in input().split()]
    print(f"Case #{i+1}: {sum([int(x) for x in input().split()]) % m}")