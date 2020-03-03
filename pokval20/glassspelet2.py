N, K, Q = [int(char) for char in input().split()]
if K == 1:
    värden = [int(char) for char in input().split()]
    for n in range(Q):
        lista = [int(char) for char in input().split()]
        if (lista[1]-lista[0]+1)%2 == 0:
            print("1")
        else:
            print("2")
if K == 2:
    värden = [int(char) for char in input().split()]
    for n in range(Q):
        L, R = [int(char) for char in input().split()]
        möjliga = R-L-1
        if möjliga%2 == 0:
            print("1")
        else:
            print("2")