t = int(input())
for case in range(t):
    n, k = [int(x) for x in input().split()]
    empdegreetotal = 0
    node, degree = [int(x) for x in input().split()]
    empdegreetotal += degree
    for i in range(1, min(n+1, k+1)):
        print(f"T {i}", flush = True)
        node, degree = [int(x) for x in input().split()]
        empdegreetotal += degree
    
    guess = round(empdegreetotal/(k+1)*n/2)
    print(f"E {guess}")