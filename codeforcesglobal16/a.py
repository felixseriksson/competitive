for case in range(int(input())):
    n, s = [int(x) for x in input().split()]
    needtofill = int(n/2) + 1
    print(int(s/needtofill))